#!/usr/bin/python3
"""
function that
divides all elements of an array by a specified number
"""


def matrix_divided(matrix, div):
    """
    function that
    divides all elements of an array by a specified number
    """
    er = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []

    if len(matrix) > 0:

        mat = len(matrix[0])

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        elif div == 0:
            raise ZeroDivisionError("division by zero")

        for fils in matrix:

            fil = []

            if len(fils) != mat:
                error = "Each row of the matrix must have the same size"
                raise TypeError(error)

            for value in fils:
                if isinstance(value, (int, float)):
                    fil.append(round(value / div, 2))

                else:
                    raise TypeError(er)

            new_matrix.append(fil)
    return new_matrix
