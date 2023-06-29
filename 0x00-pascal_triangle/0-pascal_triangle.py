#!/usr/bin/python3
"""Pascal Trinagle a triangular arrangement of numbers where each number in the triangle is the sum of the two numbers directly above it.
"""

def pascal_triangle(n):
    """ returns the pascal triangle
    """
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        # Is the first element
        list = [1]
        if i == 0:
            pascal.append(list)
            continue

       m = i-1
        for j in range(len(pascal[m])):
            if j+1 == len(pascal[m]):
                # the last element
                list.append(1)
                break

            # Add two previous values to get current next value
            nextVal = pascal[m][j] + pascal[m][j+1]
            list.append(nextVal)
        pascal.append(list)

    return pascal
