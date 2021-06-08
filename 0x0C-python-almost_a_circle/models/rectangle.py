#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """hola Duglas"""

    @property
    def width(self):
        """width method"""
        return self.__width

    """hola Duglas"""

    @property
    def height(self):
        """heigth method"""
        return self.__height

    """hola Duglas"""

    @property
    def x(self):
        """x method"""
        return self.__x

    """hola Duglas"""

    @property
    def y(self):
        """y method"""
        return self.__y

    """hola Duglas"""

    @width.setter
    def width(self, value):
        """width method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    """hola Duglas"""

    @height.setter
    def height(self, value):
        """heigth method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    """hola Duglas"""

    @x.setter
    def x(self, value):
        """x method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    """hola Duglas"""

    @y.setter
    def y(self, value):
        """y method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """public method that prints
        the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the
        Rectangle instance with the character #
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        return string[:-1]
