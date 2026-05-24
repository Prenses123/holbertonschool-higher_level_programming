#!/usr/bin/env python3
"""
This module provides a function that returns another function
capable of multiplying a float by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
