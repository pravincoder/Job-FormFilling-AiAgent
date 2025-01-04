import PyPDF2
from PyPDF2 import PdfReader
import docx
import os
import logging
from textwrap import dedent

class DocData:
    """Extract Data from documents. Supported formats are PDF, DOCX, TXT."""
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            logging.error(f'File not found: {self.file_path}')
            raise FileNotFoundError(f'File not found: {self.file_path}')
        logging.debug(f'Initialized for extracting data from {file_path}')
        self.text = None

    def extract_pdf_text(self):
        """Extract text from a PDF file."""
        try:
            logging.debug('Extracting text from PDF...')
            reader = PdfReader(self.file_path)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            self.text = text.strip()
            return self.text
        except Exception as e:
            logging.error(f'Error extracting text from PDF: {e}')
            return None

    def extract_docx_text(self):
        """Extract text from a DOCX file."""
        try:
            logging.debug('Extracting text from DOCX...')
            doc = docx.Document(self.file_path)
            text = [para.text for para in doc.paragraphs]
            return '\n'.join(text).strip()
        except Exception as e:
            logging.error(f'Error extracting text from DOCX: {e}')
            return None

    def extract_txt_text(self):
        """Extract text from a TXT file."""
        try:
            logging.debug('Extracting text from TXT...')
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except Exception as e:
            logging.error(f'Error extracting text from TXT: {e}')
            return None


# Test the class
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    file_path = 'Job_FormFilling_Agent/job_formfilling_agent/JD_ML Engineer.pdf'
    doc = DocData(file_path)
    extracted_text = dedent(doc.extract_pdf_text())
    if extracted_text:
        logging.debug('Extracted Text:')
        logging.debug(extracted_text)
    else:
        logging.error('Failed to extract text from the PDF.')
