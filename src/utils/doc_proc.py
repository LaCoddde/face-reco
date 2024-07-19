#Document processing utilities.
import PyPDF2
from docx import Document as DocxDocument
from PIL import Image
import pytesseract
import os

def process_document(document_path):
    try:
        _, file_extension = os.path.splitext(document_path)
        if file_extension.lower() in ['.pdf']:
            return process_pdf(document_path)
        elif file_extension.lower() in ['.doc', '.docx']:
            return process_docx(document_path)
        elif file_extension.lower() in ['.jpg', '.jpeg', '.png', '.heif']:
            return process_image(document_path)
        else:
            return {"status": "error", "message": "Unsupported file type"}

    except Exception as e:
        raise ValueError(f"Error in processing document: {str(e)}")

def process_pdf(document_path):
    try:
        with open(document_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extract_text()
        return {"document_data": extract_titles_and_content(text)}
    except Exception as e:
        raise ValueError(f"Error processing PDF: {str(e)}")

def process_docx(document_path):
    try:
        doc = DocxDocument(document_path)
        text = ''
        for para in doc.paragraphs:
            text += para.text + '\n'
        return {"document_data": extract_titles_and_content(text)}
    except Exception as e:
        raise ValueError(f"Error processing DOCX: {str(e)}")

def process_image(document_path):
    try:
        img = Image.open(document_path)
        text = pytesseract.image_to_string(img)
        return {"document_data": extract_titles_and_content(text)}
    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")

def extract_titles_and_content(text):
    lines = text.split('\n')
    data = {}
    current_title = None

    for line in lines:
        if line.strip() == '':
            continue

        if line.strip().isupper():
            current_title = line.strip()
            data[current_title] = []
        elif current_title:
            data[current_title].append(line.strip())

    return data