import os
from dotenv import load_dotenv
from typing import List, Tuple
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone as LangchainPinecone
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch
from pinecone import Pinecone, ServerlessSpec
from pathlib import Path

from app.loaders.markdown_loader import ViewpointMarkdownLoader
from app.loaders.html_loader import ViewpointHTMLLoader
from app.utils.file_utils import get_file_hash

load_dotenv()  # Load the .env file

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "sovllm"  # Your index name

print(f"INDEX_NAME: {INDEX_NAME}")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY must be set in .env file")

app = FastAPI()

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Check if index exists, if not create it
try:
    if INDEX_NAME not in [index.name for index in pc.list_indexes()]:
        print(f"Creating index: {INDEX_NAME}")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,  # Dimension for "sentence-transformers/all-MiniLM-L6-v2"
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws', 
                region='us-east-1'
            )
        )
        print(f"Index {INDEX_NAME} created successfully")
    else:
        print(f"Index {INDEX_NAME} already exists")
except Exception as e:
    print(f"Error checking or creating index: {e}")
    raise

# Get the index
index = pc.Index(INDEX_NAME)

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Print GPU information if available
if torch.cuda.is_available():
    print(f"CUDA Device: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Memory Allocated: {torch.cuda.memory_allocated(0) / 1024**2:.2f} MB")
    print(f"CUDA Memory Cached: {torch.cuda.memory_reserved(0) / 1024**2:.2f} MB")

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': device}
)

# Initialize vector store
vectorstore = LangchainPinecone(index, embeddings.embed_query, "text")

# Initialize language model (DeepSeek)
model_name = "deepseek-ai/deepseek-llm-7b-chat"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16, 
    device_map="auto"
)

# Set generation config for DeepSeek model
model.generation_config = GenerationConfig.from_pretrained(model_name)
model.generation_config.pad_token_id = model.generation_config.eos_token_id

class Question(BaseModel):
    text: str

    
def process_document(file_path: str):
    try:
        file_path = Path(file_path)
        file_hash = get_file_hash(str(file_path))
        
        # Check if the document is already in Pinecone
        results = index.fetch(
            ids=[file_hash],
            namespace="documents"
        )

        if results['vectors']:
            print(f"Document {file_path} already processed and in Pinecone. Skipping.")
            return

        print(f"Processing {file_path}")
        if file_path.suffix == '.pdf':
            loader = PyPDFLoader(str(file_path))
        elif file_path.suffix == '.md':
            loader = ViewpointMarkdownLoader(str(file_path))
        elif file_path.suffix in ['.htm', '.html']:
            loader = ViewpointHTMLLoader(str(file_path))
        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")

        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(documents)
        
        # Prepare vectors for upsert
        vectors = []
        for i, split in enumerate(splits):
            vector = embeddings.embed_documents([split.page_content])[0]
            vectors.append({
                "id": f"{file_hash}_{i}",
                "values": vector,
                "metadata": {
                    "text": split.page_content,
                    "source": str(file_path),
                    "file_hash": file_hash,
                    "title": split.metadata.get("title", ""),
                    "header": split.metadata.get("header", ""),
                    "header_level": split.metadata.get("header_level", 0)
                }
            })

        # Upsert to Pinecone
        print(f"Adding embeddings to Pinecone for {file_path}")
        index.upsert(vectors=vectors, namespace="documents")
    except Exception as e:
        print(f"Error processing document {file_path}: {e}")


@app.on_event("startup")
async def startup_event():
    """Process all documents in the data directory and its subdirectories on startup."""
    data_dir = Path("data")
    
    def process_directory(directory):
        for item in directory.iterdir():
            if item.is_file():
                if item.suffix in ['.md', '.htm', '.html', '.pdf']:
                    try:
                        process_document(str(item))
                    except Exception as e:
                        print(f"Error processing {item}: {e}")
            elif item.is_dir():
                process_directory(item)  # Recursively process subdirectories

    process_directory(data_dir)
    print("Finished processing all documents...")
    

@app.post("/ask")
async def ask_question(question: Question) -> Tuple[str, List[str]]:
    """Get the answer and sources for a given question."""
    try:
        # Step 1: Embed the question to get the query vector
        query_vector = embeddings.embed_query(question.text)

        # Step 2: Query the Pinecone index with the query vector
        query_results = index.query(
            namespace="documents",
            vector=query_vector,  # This is the embedded query vector
            top_k=4,  # Retrieve top 4 most similar vectors
            include_metadata=True  # Include metadata in the results
        )

        # Step 3: Extract the content from the matched documents
        if not query_results['matches']:
            return "No relevant documents found.", []

        # Combine the text from the top matches to build the context for the LLM
        context = "\n".join([match['metadata'].get('text', '') for match in query_results['matches']])

        if not context:
            return "Unable to find sufficient context for this question.", []

        # Step 4: Prepare chat messages as per DeepSeek model template
        messages = [
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question.text}"}
        ]
        input_tensor = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

        # Step 5: Generate an answer using the LLM
        outputs = model.generate(input_tensor.to(model.device), max_new_tokens=500)
        answer = tokenizer.decode(outputs[0][input_tensor.shape[1]:], skip_special_tokens=True)

        # Step 6: Retrieve sources for the answer
        sources = [match['metadata'].get('source', 'Unknown') for match in query_results['matches']]

        return answer, sources

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during question processing: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
