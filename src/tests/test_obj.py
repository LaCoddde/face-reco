#Unit tests for object detection.
import unittest
from src.services.obj_svc import detect_objects

class TestObjectDetection(unittest.TestCase):

    def test_detect_objects(self):
        result = detect_objects('dummy_image_data')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
