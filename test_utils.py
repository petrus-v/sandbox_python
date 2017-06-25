import unittest
from utils import adition

class TestUtils(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(adition(2, 2), 4)
        self.assertEqual(adition(2, 1), 3)
        self.assertEqual(adition(2, 11), 22)

