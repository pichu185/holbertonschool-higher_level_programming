#!/usr/bin/python3
"""Write a function that writes a string to a
text file (UTF8) and returns the number of
characters written
"""


def write_file(filename="", text=""):
    """writes a string"""

    with open(filename, mode="w", encoding="utf-8") as file:

        file.write("Holberton School is so cool!\n")
        
        return file.write(text)
