#!/usr/bin/python3
"""Write a class called Square"""


class Square:
    """Square class with size attribute"""
    def __init__(self, size=0):
        """size initialitation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of square"""
        area = self.__size ** 2
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
