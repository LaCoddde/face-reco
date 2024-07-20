#Controller for document data extraction
from flask import Blueprint, request, jsonify, current_app
from services.doc_svc import extract_document_data

doc_bp = Blueprint('doc', __name__)

@doc_bp.route('/', methods=['POST'])
def extract():
    if 'document' not in request.files:
        return jsonify({"status": "error", "message": "Document file is required."}), 400

    document = request.files['document']
    
    # Directory where uploaded files will be stored
    upload_folder = current_app.config['UPLOAD_FOLDER']

    results = extract_document_data(document, upload_folder)
    return jsonify(results)
