#Face-to-ID comparison algorithms.
import face_recognition

def compare_face_id(face_image_path, id_image_path):
    try:
        # Load the face and ID images
        face_image = face_recognition.load_image_file(face_image_path)
        id_image = face_recognition.load_image_file(id_image_path)
        
        # Get the face encodings
        face_encodings = face_recognition.face_encodings(face_image)
        id_encodings = face_recognition.face_encodings(id_image)
        
        if len(face_encodings) == 0:
            return {"comparison_result": "no_face_in_face_image"}
        if len(id_encodings) == 0:
            return {"comparison_result": "no_face_in_id_image"}

        # Compare faces
        face_encoding = face_encodings[0]
        id_encoding = id_encodings[0]

        results = face_recognition.compare_faces([id_encoding], face_encoding)
        comparison_result = "match" if results[0] else "no match"

        return {"comparison_result": comparison_result}
    
    except Exception as e:
        raise ValueError(f"Error in comparing face to ID: {str(e)}")