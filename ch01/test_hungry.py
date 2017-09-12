import unittest
import sys
from io import StringIO


class TestHungry(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_static(self):
        import hungry
        self.assertEqual(self.captor.getvalue(), "I'm hungry!\n")


if __name__ == '__main__':
    unittest.main()
