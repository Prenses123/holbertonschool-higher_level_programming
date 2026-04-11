#!/usr/bin/python3
"""MyList module"""


class BaseGeometry:
    """jdjdj"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("name must be an integer".format())
        if value <= 0:
            raise ValueError("name must be greater than 0".format())
        self.name = name
        self.value = value
    def area(self):
        raise Exception("area() is not implemented".format())

