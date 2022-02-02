#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Returns a pascal triangle of n size"""
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        pascal2 = []
        pascal2.append(1)
        if i == 0:
            pascal.append(pascal2)
            continue
        for j in range(1, i):
            try:
                pascal2.append(pascal[i - 1][j - 1] + pt[i - 1][j])
            except Exception:
                continue
        pascal2.append(1)
        pascal.append(pascal2)

    return pt
