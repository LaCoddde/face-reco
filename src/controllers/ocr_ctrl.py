#Controller for text recognition (OCR)
from flask import Blueprint, request, jsonify
from src.services.ocr_svc import recognize_text

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route('/', methods=['POST'])
def recognize():
    image = request.files['image']
    results = recognize_text(image)
    return jsonify(results)
