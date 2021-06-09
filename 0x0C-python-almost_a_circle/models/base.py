#!/usr/bin/python3
"""Write the first class Base"""


import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

"""static method"""

@staticmethod
def to_json_string(list_dictionaries):
    """returns the JSON string representation of list_dictionaries"""
    if list_dictionaries is None or len(list_dictionaries) == 0:
        return "[]"
    return json.dumps(list_dictionaries)
