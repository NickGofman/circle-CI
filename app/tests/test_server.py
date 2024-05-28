import unittest
import requests

class TestFlaskServer(unittest.TestCase):
    def test_server_is_up(self):
        response = None
        try:
            response = requests.get('http://127.0.0.1:8000',verify=False, timeout=5)
            self.assertEquals(response.status_code, 200, "Server is Down")
        except requests.ConnectionError:
            self.assertIsNotNone(response, "Server is Down")






