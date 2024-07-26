#Unit tests for developer account management.
import unittest
from services.account_svc import create_account, generate_api_key, revoke_api_key

class TestAccountManagement(unittest.TestCase):

    def test_create_account(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        result = create_account(data)
        self.assertEqual(result['status'], 'success')

    def test_generate_api_key(self):
        result = generate_api_key('testuser')
        self.assertEqual(result['status'], 'success')

    def test_revoke_api_key(self):
        result = revoke_api_key('testuser')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
