#!/usr/bin/python3
""" a module of Square that inherits from Rectangle (9-rectangle.py """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """this class represents a using Rectangle as a baseclass"""
    def __init__(self, size):
        """ Initializes the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """ initializes str"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
