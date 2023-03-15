import unittest
from calculator import calculate

class TestCalculate(unittest.TestCase):
    def test_valid_expression(self):
        # Test a valid expression
        self.assertEqual(calculate("2 + 3 * 4"), "14")
        
    def test_invalid_expression(self):
        # Test an invalid expression with invalid characters
        self.assertEqual(calculate("2 +& 3"), "Invalid expression!")
        
        # Test an invalid expression with division by zero
        self.assertEqual(calculate("2 / 0"), "Infinity")
        
        # Test an invalid expression with a syntax error
        self.assertEqual(calculate("2 +"), "Invalid expression!")
        
    def test_edge_cases(self):
        # Test an expression with a negative number
        self.assertEqual(calculate("-2 * 3"), "-6")
        
        # Test an expression with parentheses
        self.assertEqual(calculate("(2 + 3) * 4"), "20")
        
        # Test an expression with the percent operator
        self.assertEqual(calculate("50% + 50%"), "1.0")
        
        # Test an expression with the exponentiation operator
        self.assertEqual(calculate("2^3"), "8")
        
        # Test an expression with a decimal result
        self.assertEqual(calculate("10 / 3"), "3.33")
    
def test_modulo_operator(self):
    # Test an expression with the modulo operator
    self.assertEqual(calculate("7 % 3"), "1.0")

        
if __name__ == '__main__':
    unittest.main()
