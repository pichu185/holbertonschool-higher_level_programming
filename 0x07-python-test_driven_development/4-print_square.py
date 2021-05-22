#!/usr/bin/python3
"""Fucntion that prints a squares"""


def print_square(size):
    """takes size as parameter and prints equilateral square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
