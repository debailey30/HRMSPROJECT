import unittest
from app import connect_to_database, start_server, new_feature

class TestApp(unittest.TestCase):
    def test_connect_to_database(self):
        self.assertIsNone(connect_to_database('localhost'))

    def test_start_server(self):
        self.assertIsNone(start_server(8080))

    def test_new_feature(self):
        self.assertIsNone(new_feature())

if __name__ == '__main__':
    unittest.main()