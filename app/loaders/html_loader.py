from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document
from typing import List
import chardet
from markdownify import markdownify as md
from bs4 import BeautifulSoup

class ViewpointHTMLLoader(BaseLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        html_content = self.read_file()
        
        # Pre-process HTML to remove scripts and styles
        soup = BeautifulSoup(html_content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Extract title
        title = soup.title.string if soup.title else ""
        
        # Convert to Markdown
        markdown_content = md(str(soup), 
                              heading_style="ATX",
                              bullets="*+-",
                              autolinks=True,
                              default_title=True,
                              escape_asterisks=False,
                              escape_underscores=False,
                              newline_style="BACKSLASH",
                              strip=['a'])  # Strip out <a> tags to avoid issues with JavaScript popups

        return [Document(page_content=markdown_content, metadata={"source": self.file_path, "title": title})]

    def read_file(self) -> str:
        # First, try reading as UTF-8
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # If UTF-8 fails, detect encoding
            with open(self.file_path, 'rb') as file:
                raw_data = file.read()
                detected = chardet.detect(raw_data)
                encoding = detected['encoding']

            # Read file with detected encoding
            try:
                with open(self.file_path, 'r', encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                # If all else fails, read with 'replace' error handler
                with open(self.file_path, 'r', encoding='utf-8', errors='replace') as file:
                    return file.read()