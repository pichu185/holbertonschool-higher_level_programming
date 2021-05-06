#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    matrix_1 = []
    for i in matrix:
        matrix_1.append(list(map((lambda x: x * x), i)))
    return matrix_1
