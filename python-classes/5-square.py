#!/usr/bin/python3
"""Square class with private size, getter, setter, area, and print."""


class Square:
    """Defines a square with a size attribute."""

    def __init__(self, size=0):
        """Initialize the square with optional size."""
        self.size = size  # setter çağırılır və yoxlama aparılır

    @property
    def size(self):
        """Getter: returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: validates and sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
