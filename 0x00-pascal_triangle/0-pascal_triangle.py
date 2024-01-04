#!/usr/bin/python3
"""
funct def pascal_triangle(n): returns a list of lists of int
representing Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of int representing the Pascal's
    triangle of n

    Args:
        n (int): num of rows

    Returns:
        list: int representing Pascal's triangle.
    """
    # if n is less or 0 return an empty list
    if n <= 0:
        return []

    else:
        # Initialize a variable called triangle with a list
        triangle = [[1]]

        for i in range(1, n):
            # Iteration of the loop, a new list is created
            triangle.append([1])

            # Function then enters a nested loop
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])

            # Process continues until all of the elements in the new row
            triangle[i].append(1)
        return triangle
