#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Pascal's Triangle"""

    if n <= 0:
        return []
    
    for i in range(n):
        
