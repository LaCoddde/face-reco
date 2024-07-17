#Unit tests for face-to-ID image comparison.
import unittest
from src.services.compare_svc import compare_faces

class TestFaceComparison(unittest.TestCase):

    def test_compare_faces(self):
        result = compare_faces('dummy_face_image', 'dummy_id_image')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
