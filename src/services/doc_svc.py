#Service for document data extraction
from werkzeug.utils import secure_filename
import os
from src.utils.doc_proc import process_document

def extract_document_data(document, upload_folder):
    try:
        if not document:
            return {"status": "error", "message": "Document is required."}

        # Secure the filename
        document_filename = secure_filename(document.filename)
        
        # Save the file to the upload folder
        document_path = os.path.join(upload_folder, document_filename)
        document.save(document_path)
        
        # Process the document
        document_data = process_document(document_path)
        
        # Clean up the saved file
        os.remove(document_path)
        
        return {"status": "success", "message": "Document data extracted", "data": document_data}

    except Exception as e:
        return {"status": "error", "message": str(e)}