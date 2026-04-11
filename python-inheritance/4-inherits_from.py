#!/usr/bin/python3
"""MyList module"""


def inherits_from(obj, a_class):
    "asddd"
    return type(obj) is not a_class and isinstance(type(obj), a_class)
