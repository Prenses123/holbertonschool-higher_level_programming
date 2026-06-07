#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
import os

# Bu sətirlər test faylının yerləşdiyi qovluqdan bir üst qovluğu (ana qovluğu)
# Python-un axtarış sisteminə (sys.path) əlavə edir.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_regular_list(self):
        """Test a normal ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the first index."""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with only a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats_list(self):
        """Test a list containing float numbers."""
        self.assertEqual(max_integer([1.53, 6.33, -2.5, 4.2]), 6.33)

    def test_ints_and_floats(self):
        """Test a list with a mix of integers and float numbers."""
        self.assertEqual(max_integer([1, 2.5, 9, 4.5]), 9)

    def test_negative_numbers(self):
        """Test a list with only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -9, -2]), -1)

    def test_all_equal_numbers(self):
        """Test a list where all elements are identical."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
