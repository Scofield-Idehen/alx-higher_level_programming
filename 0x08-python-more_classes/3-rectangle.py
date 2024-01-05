#!/usr/bin/python3
"""Write imported module here"""


class Rectangle:
    """Represents a rect"""

    def __init__(self, width=0, height=0):
        """ "Initializes the rect

        Args:
            width: width of the rect
            height: height of the rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method of the width

        Returns: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for d width

        Args:
            value: width's val

        Raises:
            TypeError: if width is not an integer
            ValueError: if width less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method of d height

        Returns: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for d height

        Args:
            value: height val

        Raises:
            TypeError: if val is not an integer
            ValueError: if value < 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method that return d perimeter of the rectangle
        """
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Return the string representation of d rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height).strip()
