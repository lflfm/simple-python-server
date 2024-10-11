import unittest
from app import app

class FlaskServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_app_test_status_good_or_bad(self):
        # Arrange
        url = '/app-test-status?deviceId=test_device'
        
        # Act
        response = self.app.get(url)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn(data['status'], ['GOOD', 'BAD'])

    def test_app_test_status_missing_device_id(self):
        # Arrange
        url = '/app-test-status'
        
        # Act
        response = self.app.get(url)
        
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid request, missing deviceId', response.data)

    def test_invalid_route(self):
        # Arrange
        url = '/'
        
        # Act
        response = self.app.get(url)
        
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid route', response.data)

if __name__ == '__main__':
    unittest.main()