#!/usr/bin/python3
""" Defines square with size """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the data.
        Args: size - represents the size of the square defined.
        Must be int and > 0.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ retrieves size of square """

        return self.__size

    @size.setter
    def size(self, value):
        """ Sets Size """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return: area of the square """

        return self.__size * self.__size

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
