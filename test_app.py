import unittest
from app import connect_to_database, start_server

class TestApp(unittest.TestCase):
    def test_connect_to_database(self):
        self.assertIsNone(connect_to_database('localhost'))

    def test_start_server(self):
        self.assertIsNone(start_server(8080))

if __name__ == '__main__':
    unittest.main()