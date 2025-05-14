import unittest
from addition import add

class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -10), -15)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_mixed_signs(self):
        self.assertEqual(add(5, -10), -5)

if __name__ == "__main__":
    unittest.main()
