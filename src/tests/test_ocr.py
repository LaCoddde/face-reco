#Unit tests for text recognition (OCR).
import unittest
from services.ocr_svc import recognize_text

class TestOCR(unittest.TestCase):

    def test_recognize_text(self):
        result = recognize_text('dummy_image_data')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
