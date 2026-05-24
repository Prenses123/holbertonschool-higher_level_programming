#!/usr/bin/env python3
"""
This module provides a type-annotated function to sum a mixed list of numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates and returns the sum of a list containing ints and floats."""
    return float(sum(mxd_lst))
