#!/usr/bin/python3
"""This module has the base class"""


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initalizes classmintances"""
        if id i is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
