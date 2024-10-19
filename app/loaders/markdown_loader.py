from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document
import markdown
from bs4 import BeautifulSoup
import re
from typing import List

class ViewpointMarkdownLoader(BaseLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Convert Markdown to HTML
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')

        documents = []

        # Process headers and their contentD
        for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            header_text = header.get_text()
            content = ""
            for sibling in header.next_siblings:
                if sibling.name and sibling.name.startswith('h'):
                    break
                content += str(sibling)

            # Clean up the content
            content = re.sub(r'\n+', '\n', content).strip()

            doc = Document(
                page_content=f"{header_text}\n\n{content}",
                metadata={
                    "source": self.file_path,
                    "header": header_text,
                    "header_level": int(header.name[1])
                }
            )
            documents.append(doc)

        return documents