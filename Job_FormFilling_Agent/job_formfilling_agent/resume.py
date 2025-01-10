import PyPDF2
from PyPDF2 import PdfReader
import docx
import os
import logging
from textwrap import dedent
import gradio as gr

def extract_text_from_file(file):
    if file is None:
        return "No file uploaded!"
    
    # Determine file type
    file_type = file.name.split('.')[-1].lower()
    
    text = ""
    try:
        if file_type == "pdf":
            # Extract text from PDF
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        elif file_type == "docx":
            # Extract text from DOCX
            doc = docx.Document(file)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        elif file_type == "txt":
            # Extract text from TXT
            text = file.read().decode("utf-8")
        else:
            return "Unsupported file type! Please upload a PDF, DOCX, or TXT file."
    except Exception as e:
        return f"Error reading file: {str(e)}"
    
    return text.strip()
