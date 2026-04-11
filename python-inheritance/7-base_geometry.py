#!/usr/bin/python3
"""MyList module"""


class BaseGeometry:
    """jdjdj"""
    def area(self):
        raise Exception("area() is not implemented".format())
    def __init__(self):
        def integer_validator(self, name, value):
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(self.name))
            if self.value <= 0:
                raise ValueError("{} must be greater than 0".format(self.name))
            self.name = name
            self.value = value


