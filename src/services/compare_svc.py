#Service for face-to-ID image comparison
from utils.compare import compare_face_id
from werkzeug.utils import secure_filename
import os

def compare_faces(face_image, id_image, upload_folder):
    try:
        if not face_image or not id_image:
            return {"status": "error", "message": "Both face image and ID image are required."}

        # Secure the filenames
        face_image_filename = secure_filename(face_image.filename)
        id_image_filename = secure_filename(id_image.filename)

        # Save the files to the upload folder
        face_image_path = os.path.join(upload_folder, face_image_filename)
        id_image_path = os.path.join(upload_folder, id_image_filename)
        
        face_image.save(face_image_path)
        id_image.save(id_image_path)

        # Perform the face-to-ID image comparison
        result = compare_face_id(face_image_path, id_image_path)
        
        # Clean up the saved files
        os.remove(face_image_path)
        os.remove(id_image_path)
        
        return {"status": "success", "message": "Faces compared", "result": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}
