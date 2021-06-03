#!/usr/bin/python3
"""WWrite a function that creates an Object
from a “JSON file”:
"""


import json
from os import waitpid


def load_from_json_file(filename):
    """creates object from JSON file"""

    with open(filename, mode="r", encoding="utf-8") as file:
    return json.load(file)
    