#Controller for document data extraction
from flask import Blueprint, request, jsonify
from src.services.doc_svc import extract_document_data

doc_bp = Blueprint('doc', __name__)

@doc_bp.route('/', methods=['POST'])
def extract():
    document = request.files['document']
    results = extract_document_data(document)
    return jsonify(results)
