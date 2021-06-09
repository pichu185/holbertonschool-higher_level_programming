#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """__str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """size method"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method that assigns attributes:
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if len(args) is not 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)
