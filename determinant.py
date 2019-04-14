import numpy as np


def finding_determinant(matrix) -> int:
    opr1 = matrix[0][0]*matrix[1][1]*matrix[2][2]
    opr2 = matrix[0][1]*matrix[1][2]*matrix[2][0]
    opr3 = matrix[0][2]*matrix[1][0]*matrix[2][1]
    opr4 = matrix[0][2]*matrix[1][1]*matrix[2][0]
    opr5 = matrix[0][0]*matrix[1][2]*matrix[2][1]
    opr6 = matrix[0][1]*matrix[1][0]*matrix[2][2]
    found_determinant = opr1 + opr2 + opr3 - opr4 - opr5 - opr6
    return found_determinant
