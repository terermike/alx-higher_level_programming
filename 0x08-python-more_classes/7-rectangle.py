#!/usr/bin/python3
""" This is the "Rectangle"  module."""


class Rectangle:
    """a simple Rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the obects """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieves widht """
        return self.__width

    @width.setter
    def width(self, value):
        """"sets the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area"""
        return self.__height * self.__width

    def perimeter(self):
        """ calculates perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """ return a string representation of the rectangle """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints message when an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
