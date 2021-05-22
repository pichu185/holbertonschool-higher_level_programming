#!/usr/bin/python3


def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError(
            ("matrix must be a matrix (list of lists) of integers/floats")
   
   