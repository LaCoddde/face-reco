#service for face recognition services
from werkzeug.utils import secure_filename
import os
from src.utils.face_recog import detect_faces

def recognize_face(image, upload_folder):
    try:
        if not image:
            return {"status": "error", "message": "Image is required."}

        # Secure the filename
        image_filename = secure_filename(image.filename)
        
        # Save the file to the upload folder
        image_path = os.path.join(upload_folder, image_filename)
        image.save(image_path)
        
        # Detect faces and extract attributes
        results = detect_faces(image_path)
        
        # Clean up the saved file
        os.remove(image_path)
        
        return {"status": "success", "message": "Face recognized", "data": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}