#Controller for object detection
from flask import Blueprint, request, jsonify, current_app, render_template
from services.obj_svc import detect_objects

obj_bp = Blueprint('obj', __name__)

@obj_bp.route('/', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({"status": "error", "message": "Image file is required."}), 400

        image = request.files['image']
        
        # Directory where uploaded files will be stored
        upload_folder = current_app.config['UPLOAD_FOLDER']
        
        results = detect_objects(image, upload_folder)
        return jsonify(results)
    return render_template('object_detection.html')

