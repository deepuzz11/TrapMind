import unittest
from app import app

class TestTrapMind(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    def test_homepage(self):
        """Test that the homepage loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_alert(self):
        """Test sending an alert"""
        response = self.client.get('/alert')
        self.assertIn(b"Alert Sent", response.data)

if __name__ == '__main__':
    unittest.main()
