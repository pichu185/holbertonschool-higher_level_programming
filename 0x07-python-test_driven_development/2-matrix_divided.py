#!/usr/bin/python3
"""Function to divide a matrix by a constant"""


def matrix_divided(matrix, div):
    """This function takes a matrix and divides every element by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if type(matrix) is not list or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
   
