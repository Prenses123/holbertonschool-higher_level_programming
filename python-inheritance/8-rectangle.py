#!/usr/bin/python3
"""MyList module"""


class BaseGeometry:
    """jdjdj"""
    def area(self):
        raise Exception("area() is not implemented".format())

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """hdhfh"""
    def __init__(self, name, value, width, height):
        super().__init__(name,value)
        def integer_validator(self, width, height):
            if width < 0 or height < 0:
                return False
    self.__width = width
    self.__height = height
