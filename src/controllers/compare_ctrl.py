# Controller for face-to-ID image comparison
from flask import Blueprint, request, jsonify, current_app
from src.services.compare_svc import compare_faces

compare_bp = Blueprint('compare', __name__)

@compare_bp.route('/', methods=['POST'])
def compare():
    if 'face_image' not in request.files or 'id_image' not in request.files:
        return jsonify({"status": "error", "message": "Face image and ID image are required."}), 400

    face_image = request.files['face_image']
    id_image = request.files['id_image']

    # Directory where uploaded files will be stored
    upload_folder = current_app.config['UPLOAD_FOLDER']

    results = compare_faces(face_image, id_image, upload_folder)
    return jsonify(results)