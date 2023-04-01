import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from calculator import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("2 + 3"), "5")

    def test_subtraction(self):
        self.assertEqual(calculate("5 - 2"), "3")

    def test_multiplication(self):
        self.assertEqual(calculate("2 * 3"), "6")

    def test_division(self):
        self.assertEqual(calculate("6 / 3"), "2.0")

    def test_division_by_zero(self):
        self.assertEqual(calculate("2 / 0"), "Infinity")

    def test_negative_number(self):
        self.assertEqual(calculate("-2 * 3"), "-6")

    def test_parentheses(self):
        self.assertEqual(calculate("(2 + 3) * 4"), "20")

    def test_percent_operator(self):
        self.assertEqual(calculate("50% + 50%"), "1.0")

    def test_exponentiation_operator(self):
        self.assertEqual(calculate("2^3"), "8")

    def test_decimal_result(self):
        self.assertEqual(calculate("10 / 3"), "3.33")

    def test_invalid_expression(self):
        self.assertEqual(calculate("2 +& 3"), "Invalid expression!")
        self.assertEqual(calculate("2 +"), "Invalid expression!")


if __name__ == '__main__':
    unittest.main()
