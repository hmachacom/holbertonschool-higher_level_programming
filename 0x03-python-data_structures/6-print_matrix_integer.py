#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = len(matrix)
    for i in range(0, idx):
        idx2 = len(matrix[i])
        for j in range(0, idx2):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("")
