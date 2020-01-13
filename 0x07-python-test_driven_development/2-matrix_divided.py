#!/usr/bin/python3


def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of list)"
                        " of integers/floats")
    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of list)"
                        " of integers/floats")
    if not all(len(i) > 0 for i in matrix):
        raise TypeError("matrix must be a matrix (list of list)"
                        " of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix mus have the same size")
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of list)"
                            " of integers/floats")
        if not all(isinstance(j, (int, float)) for j in i):
            raise TypeError("matrix must be a matrix (list of list)"
                            " of integers/floats")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new = []
    for i in matrix:
        new.append(list(map(lambda j: round(j / div, 2), i)))
    return new
