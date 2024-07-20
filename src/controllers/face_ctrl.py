#Controller for face recognition.
from flask import Blueprint, request, jsonify, current_app
from services.face_svc import recognize_face

face_bp = Blueprint('face', __name__)

@face_bp.route('/', methods=['POST'])
def recognize():
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "Image file is required."}), 400

    image = request.files['image']

    # Directory where uploaded files will be stored
    upload_folder = current_app.config['UPLOAD_FOLDER']

    results = recognize_face(image, upload_folder)
    return jsonify(results)
