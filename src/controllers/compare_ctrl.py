# Controller for face-to-ID image comparison
from flask import Blueprint, request, jsonify
from src.services.compare_svc import compare_faces

compare_bp = Blueprint('compare', __name__)

@compare_bp.route('/', methods=['POST'])
def compare():
    face_image = request.files['face_image']
    id_image = request.files['id_image']
    results = compare_faces(face_image, id_image)
    return jsonify(results)
