#!/usr/bin/python3
""" This is a square module which is a subclass of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes Square"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints Square's properties"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """gets size"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets width and height"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        sq = {'id': self.id, 'size': self.size , 'x': self.x,
              'y': self.y}
        return sq
