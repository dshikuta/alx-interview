#!/usr/bin/python3
"""Pascal Trinagle a triangular arrangement of numbers where each number in the triangle is the sum of the two numbers directly above it.
"""

def pascal_triangle(n):
    """returns the pascal triangle
    """

    if n <= 0:
        return []

    pascal = []

        for i in range(n):
       list = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                list[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(list)
"""add two previous numbers
"""

    return pascal
