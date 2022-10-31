#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the Rectangle's area"""
        return self.__height * self.__width

    def display(self):
        """that prints in stdout the Rectangle instance with
        the character # """
        for y in range(self.__y):
            print("")
        for x in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """prints Rectangle's info"""
        s = "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        **kwargs must be skipped if *args exists and is not empty
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        super.__init__(id)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        super().__init__(id)
                    else:
                        self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        re_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x,
                   'y': self.__y}
        return re_dict
