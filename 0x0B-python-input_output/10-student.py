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
        if type(attrs) is list and (type(i) is str for i in attrs):