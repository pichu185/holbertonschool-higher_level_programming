#!/usr/bin/python3
"""Write the first class Base"""


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.if = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
