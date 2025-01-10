import unittest
from src.main import app  # Assuming 'app' is the main application function

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_buyer_preferences(self):
        response = self.app.post('/generate_narrative', json={
            'neighborhood': 'Downtown',
            'price': 500000,
            'bedrooms': 3,
            'bathrooms': 2,
            'house_size': 1500
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('narrative', response.json)

if __name__ == '__main__':
    unittest.main()