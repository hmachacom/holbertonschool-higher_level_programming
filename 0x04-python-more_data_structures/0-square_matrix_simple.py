#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for i in range(len(matrix)):
            arry = []
            for j in range(len(matrix[i])):
                sqr = matrix[i][j]
                arry.append(sqr * sqr)
            new_matrix.append(arry)
        return new_matrix
