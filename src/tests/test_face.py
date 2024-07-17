#Unit tests for face recognition.
import unittest
from src.services.face_svc import recognize_face

class TestFaceRecognition(unittest.TestCase):

    def test_recognize_face(self):
        result = recognize_face('dummy_image_data')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
