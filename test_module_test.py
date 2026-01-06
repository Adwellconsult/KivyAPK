"""
Unit tests for test_module.
"""

import unittest
from test_module import add, subtract, multiply, greet


class TestMathFunctions(unittest.TestCase):
    """Test cases for mathematical functions."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(20, 8), 12)
    
    def test_subtract_negative_numbers(self):
        """Test subtracting with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(10, -5), 15)
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(7, 8), 56)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 10), 0)


class TestGreetFunction(unittest.TestCase):
    """Test cases for the greet function."""
    
    def test_greet_simple_name(self):
        """Test greeting with a simple name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
    
    def test_greet_empty_string(self):
        """Test greeting with an empty string."""
        self.assertEqual(greet(""), "Hello, !")
    
    def test_greet_with_spaces(self):
        """Test greeting with names containing spaces."""
        self.assertEqual(greet("John Doe"), "Hello, John Doe!")


if __name__ == '__main__':
    unittest.main()
