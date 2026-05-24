#!/usr/bin/env python3
"""
This module provides a type-annotated function that returns a tuple
containing a string and the square of a number as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is k and the second is v squared."""
    return (k, float(v ** 2))
