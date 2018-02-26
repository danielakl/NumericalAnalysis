import numpy as np


def gausselim(matrix):
    dimensions = matrix.shape
    rows = dimensions[0]
    cols = dimensions[1]
    matrix = np.copy(matrix)

    for j in range(0, rows - 1):
        for i in range(j + 1, rows):
            multiplier = (matrix[i, j] / matrix[j, j])
            for k in range(j, cols):
                matrix[i, k] = matrix[i, k] - matrix[j, k] * multiplier
    return matrix


def back_substitute(matrix):
    dimensions = matrix.shape
    rows = dimensions[0]
    cols = dimensions[1]

    if cols - 1 == rows:
        result = [None] * rows
        for j in range(rows - 1, 0):
            result[j] =



def main():
    # Solve system:
    # -------------
    #  2x - 2y -  z = -2
    #  4x +  y - 2z =  1
    # -2x +  y -  z = -3
    # matrix = np.array([[2.0, -2.0, -1.0, -2.0],
    #                    [4.0, 1.0, -2.0, 1.0],
    #                    [-2.0, 1.0, -1.0, -3.0]])
    # result = gausselim(matrix)
    # print("x = ", result[0])
    # print("y = ", result[1])
    # print("z = ", result[2], "\n")

    # Solve system:
    # -------------
    #  x + 2y - z = 2
    #      3y + z = 4
    # 2x -  y + z = 2
    matrix = np.array([[1.0, 2.0, -1.0, 2.0],
                       [0.0, 3.0, 1.0, 4.0],
                       [2.0, -1.0, 1.0, 2.0]])
    # result = gausselim(matrix)
    print(gausselim(matrix))
    # print("x = ", result[0])
    # print("y = ", result[1])
    # print("z = ", result[2], "\n")

    # Solve system:
    # 2x +  y - 4z = -7
    #  x -  y +  z = -2
    # -x + 3y - 2z =  6
    # matrix = np.array([[2.0, 1.0, -4.0, -7.0],
    #                    [1.0, -1.0, 1.0, -2.0],
    #                    [-1.0, 3.0, -2.0, 6.0]])
    # result = gausselim(matrix)
    # print("x = ", result[0])
    # print("y = ", result[1])
    # print("z = ", result[2], "\n")

    return 1


main()
