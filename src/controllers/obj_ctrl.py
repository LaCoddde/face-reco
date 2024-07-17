#Controller for object detection
from flask import Blueprint, request, jsonify
from src.services.obj_svc import detect_objects

obj_bp = Blueprint('obj', __name__)

@obj_bp.route('/', methods=['POST'])
def detect():
    image = request.files['image']
    results = detect_objects(image)
    return jsonify(results)
