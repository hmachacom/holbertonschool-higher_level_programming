#!/usr/bin/python3
"""::::::::::::::::::"""


def pascal_triangle(n):
    """:::::::::::::::::::::"""
    pt = []
    if n <= 0:
        return pt
    for i in range(n):
        pl = []
        pl.append(1)
        if i == 0:
            pt.append(pl)
            continue
        for j in range(1, i):
            try:
                pl.append(pt[i - 1][j - 1] + pt[i - 1][j])
            except:
                continue
        pl.append(1)
        pt.append(pl)

    return pt
