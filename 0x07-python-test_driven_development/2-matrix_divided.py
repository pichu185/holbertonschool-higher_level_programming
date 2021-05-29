#!/usr/bin/python3
"""Function to divide a matrix by a constant"""


def matrix_divided(matrix, div):
    """This function takes a matrix and divides every element by div"""
    if type(matrix) is not list or matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        for i in row:
            if type(i) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    len_0 = len(matrix[0]):
    for j in matrix:
        if len(j) is not len[0]:
            raise TypeError("Each row of the matrix must have the same size")
       
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
   