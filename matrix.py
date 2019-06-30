import numpy as np

# def matrix_determinant_2x2(matrix) -> int:
#     opr1 = matrix[0][0]*matrix[1][1]
#     opr2 = matrix[0][1]*matrix[1][0]
#     found_determinant = opr1 - opr2
#     return found_determinant


# def matrix_determinant_2x2_in_label(matrix) -> int:
#     el1 = matrix[0][0]
#     el2 = matrix[0][1]
#     el3 = matrix[1][0]
#     el4 = matrix[1][1]
#     return el1, el2, el3, el4


def matrix_3x3(matrix) -> int:
    opr1 = matrix[0][0]*matrix[1][1]*matrix[2][2]
    opr2 = matrix[0][1]*matrix[1][2]*matrix[2][0]
    opr3 = matrix[0][2]*matrix[1][0]*matrix[2][1]
    opr4 = matrix[0][2]*matrix[1][1]*matrix[2][0]
    opr5 = matrix[0][0]*matrix[1][2]*matrix[2][1]
    opr6 = matrix[0][1]*matrix[1][0]*matrix[2][2]
    found_determinant = opr1 + opr2 + opr3 - opr4 - opr5 - opr6
    return found_determinant


# matrix = np.array([[4, 2, 4, 5],
#                     [1, 2, 6, 7],
#                     [2, 4, 5, 7],
#                     [4, 6, 7, 4]])


def finding_determinant_four_order(matrix) -> int:
    a11 = matrix[0][0]
    a12 = matrix[0][1]
    a13 = matrix[0][2]
    a14 = matrix[0][3]

    matrix_1 = np.array([[matrix[1][1], matrix[1][2], matrix[1][3]],
                         [matrix[2][1], matrix[2][2], matrix[2][3]],
                         [matrix[3][1], matrix[3][2], matrix[3][3]]])

    matrix_2 = np.array([[matrix[1][0], matrix[1][2], matrix[1][3]],
                         [matrix[2][0], matrix[2][2], matrix[2][3]],
                         [matrix[3][0], matrix[3][2], matrix[3][3]]])

    matrix_3 = np.array([[matrix[1][0], matrix[1][1], matrix[1][3]],
                         [matrix[2][0], matrix[2][1], matrix[2][3]],
                         [matrix[3][0], matrix[3][1], matrix[3][3]]])

    matrix_4 = np.array([[matrix[1][0], matrix[1][1], matrix[1][2]],
                         [matrix[2][0], matrix[2][1], matrix[2][2]],
                         [matrix[3][0], matrix[3][1], matrix[3][2]]])

    part1 = a11*matrix_3x3(matrix_1) - a12*matrix_3x3(matrix_2)
    part2 = a13*matrix_3x3(matrix_3) - a14*matrix_3x3(matrix_4)
    found_determinant = part1 + part2
    return found_determinant
