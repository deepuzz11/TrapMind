import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_attack_data(self):
        response = self.app.get('/get_attack_data')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('attack_type', data)
        self.assertIn('details', data)

if __name__ == '__main__':
    unittest.main()
