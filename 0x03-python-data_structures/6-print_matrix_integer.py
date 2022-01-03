#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = len(matrix)
    space = " "
    for i in range(0, idx):
        idx2 = len(matrix[i])
        for j in range(0, idx2):
            print("{:d}{:s}".format(matrix[i][j], space), end="")
            space = " "
        print()
