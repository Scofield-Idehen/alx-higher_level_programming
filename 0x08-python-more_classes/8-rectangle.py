#!/usr/bin/python3
"""Write imported module here"""


class Rectangle:
    """Represents a rect"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ "Initializes the rectangle
        Args:
            width: width of the rect
            height: height of the rect
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """getter method of the width
        Returns: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width
        Args:
            value: width's value

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
        """getter method of the height
        Returns: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height
        Args:
            value: height value

        Raises:
            TypeError: if value is not an integer
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
        Method that return the perimeter of the rectangle
        """
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Return the string representation of rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        result = (str(self.print_symbol) * self.width + "\n") * self.height
        return result.strip()

    def __repr__(self):
        """Return the formal representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Detect instance deletion
        """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method that returns biggest rectangle based on the area
        Args:
            rect_1: rectangle one
            rect_2: rectangle two
        Raises:
            TypeError: if rect_1 or rect_2 are not rectangles
        Returns:
            rect_1 if both have  same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
