#!/usr/bin/python3
""" Defines square with size """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the data.
        Args: size - represents the size of the square defined. Must be int.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
