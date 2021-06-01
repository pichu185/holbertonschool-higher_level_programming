#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width, height):

    self.__width = width
    self.__height = height
    self.integer_validator("width", width)
    self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
