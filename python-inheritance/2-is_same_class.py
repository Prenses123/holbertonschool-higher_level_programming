#!/usr/bin/python3
"""MyList module"""


def is_same_class(obj, a_class):
    """jdjjdj"""
    if type(a_class) == int:
        return False
    if isinstance(obj, a_class):
        return True
    return False
