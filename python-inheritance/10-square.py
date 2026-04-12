#!/usr/bin/python3
"hjdsfkhd"
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    "dgdfgd"
    def __init__(self, size):
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

