#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    power = []
    for y in matrix:
        power.append(list((map(lambda y: y ** 2, y))))
    return power
