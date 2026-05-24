#!/usr/bin/env python3
"""
This module provides a type-annotated function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates and returns the sum of a list of floats."""
    return sum(input_list)
