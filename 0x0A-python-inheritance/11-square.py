#!/usr/bin/python3
"""Module for Square, inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """is a sublass of Rectangle"""
    def __init__(self, size):
        """Constructor method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Func dat cal the area of square"""
        return self.__size * self.__size
