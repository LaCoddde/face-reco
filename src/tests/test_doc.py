#Unit tests for document data extraction.
import unittest
from services.doc_svc import extract_document_data

class TestDocumentExtraction(unittest.TestCase):

    def test_extract_document_data(self):
        result = extract_document_data('dummy_document_data')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
