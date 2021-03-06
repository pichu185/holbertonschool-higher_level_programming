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
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """__str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if len(args) is not 0:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Public method that returns the dictionary representation
        of a Rectangle
        """
        return{"id": self.id, "width": self.__width,
               "height": self.__height, "x": self.__x, "y": self.__y}
