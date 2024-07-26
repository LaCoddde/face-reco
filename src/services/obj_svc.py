#Service for object detection
from werkzeug.utils import secure_filename
import os
from utils.obj_detect import process_image

def detect_objects(image, upload_folder):
    try:
        if not image:
            return {"status": "error", "message": "Image is required."}

        # Secure the filename
        image_filename = secure_filename(image.filename)
        
        # Save the file to the upload folder
        image_path = os.path.join(upload_folder, image_filename)
        image.save(image_path)
        
        # Process the image
        detection_results = process_image(image_path)
        
        # Clean up the saved file
        os.remove(image_path)
        
        return {"status": "success", "message": "Objects detected", "data": detection_results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
