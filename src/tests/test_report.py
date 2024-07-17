#Unit tests for analytics and reporting.
import unittest
from src.services.report_svc import get_analytics

class TestReporting(unittest.TestCase):

    def test_get_analytics(self):
        result = get_analytics()
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
