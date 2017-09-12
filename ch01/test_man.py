import unittest
import sys
from io import StringIO


class TestMan(unittest.TestCase):

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_static(self):
        import man
        self.assertEqual(self.captor.getvalue(), "Initialized!\nHello David!\nGood-bye David!\n")


if __name__ == '__main__':
    unittest.main()
