#!/usr/bin/python3
"""Write a class Student that defines
a student by: (based on 9-student.py)
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictionary = {}
        if attrs is not None:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__.update({i: json[i]})
