import unittest

from flaskapp import app

class TestApp(unittest.TestCase):
    
        def setUp(self):
            self.app = app.test_client()
    
        def test_hello_world(self):
            response = self.app.get('/')
            self.assertEqual(response.data, b'Hello JENKINS with everything!')

if __name__ == '__main__':
    unittest.main()
