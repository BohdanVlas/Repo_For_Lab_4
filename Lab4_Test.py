import unittest
import Lab4 as test_lab
import json

class LabTests(unittest.TestCase):

    def setUp(self):
        self.app = test_lab.app.test_client()

    def test_get_hello(self):
        r = self.app.get('/')
        self.assertEqual(r._status_code, 200)
        self.assertEqual(r.get_data(), b'Hello world!!! This app testing pipeline.')

if __name__ == '__name__':
    unittest.main()