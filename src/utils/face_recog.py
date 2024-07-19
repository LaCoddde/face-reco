#Face recognition algorithms
import cv2
import numpy as np
import dlib
from PIL import Image
from deepface import DeepFace

def detect_faces(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = detector(gray)
        
        results = []
        for face in faces:
            # Convert the face region to a path for analysis
            (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
            face_image = image[y:y+h, x:x+w]
            face_image_path = "/tmp/face_image.jpg"
            cv2.imwrite(face_image_path, face_image)
            
            # Get detailed attributes
            age = estimate_age(face_image_path)
            gender = estimate_gender(face_image_path)
            eye_color = estimate_eye_color(face_image_path)
            
            results.append({
                "coordinates": {
                    "left": face.left(),
                    "top": face.top(),
                    "right": face.right(),
                    "bottom": face.bottom()
                },
                "age_estimate": age,
                "gender": gender,
                "eye_color": eye_color
            })
        
        return {"faces": results}
    
    except Exception as e:
        raise ValueError(f"Error in detecting faces: {str(e)}")

def estimate_age(face_image_path):
    try:
        # Use DeepFace to analyze the face image
        analysis = DeepFace.analyze(face_image_path, actions=['age'])
        # Extract the age estimate from the analysis
        age = analysis[0]['age']
        return f"{age-5}-{age+5}"  # Return an age range
    except Exception as e:
        raise ValueError(f"Error in estimating age: {str(e)}")

def estimate_gender(face_image_path):
    try:
        # Use DeepFace to analyze the face image
        analysis = DeepFace.analyze(face_image_path, actions=['gender'])
        # Extract the gender from the analysis
        gender = analysis[0]['gender']
        return gender
    except Exception as e:
        raise ValueError(f"Error in estimating gender: {str(e)}")

def estimate_eye_color(face_image):
    try:
        # Convert the face image to RGB
        image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        
        # Convert to HSV color space for better color detection
        eye_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
        
        # Define color ranges in HSV
        color_ranges = {
            "Brown": ((10, 50, 50), (20, 255, 255)),
            "Blue": ((100, 50, 50), (130, 255, 255)),
            "Green": ((35, 50, 50), (85, 255, 255)),
            "Gray": ((0, 0, 50), (0, 0, 200))
        }
        
        # Determine eye color
        eye_color = "Unknown"
        for color, (lower, upper) in color_ranges.items():
            mask = cv2.inRange(eye_hsv, np.array(lower), np.array(upper))
            if cv2.countNonZero(mask) > 0:
                eye_color = color
                break
        
        return eye_color
    
    except Exception as e:
        raise ValueError(f"Error in estimating eye color: {str(e)}")

