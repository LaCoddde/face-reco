#Controller for face recognition.
from flask import Blueprint, request, jsonify
from src.services.face_svc import recognize_face

face_bp = Blueprint('face', __name__)

@face_bp.route('/', methods=['POST'])
def recognize():
    image = request.files['image']
    results = recognize_face(image)
    return jsonify(results)
