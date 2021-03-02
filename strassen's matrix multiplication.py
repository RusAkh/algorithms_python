import numpy as np
from random import randint


def squared_matrix(size, *elements):
    return np.array(elements).reshape(size, size)


def strassen_n_by_n(matrix1, matrix2):
    width = height = len(matrix1)
    breakpoint_ = int(width / 2)
    if width == 1 or height == 1:
        return matrix1.dot(matrix2)

    A = matrix1[:breakpoint_, :breakpoint_]  # find quarters
    B = matrix1[:breakpoint_, breakpoint_:]
    C = matrix1[breakpoint_:, :breakpoint_]
    D = matrix1[breakpoint_:, breakpoint_:]
    E = matrix2[:breakpoint_, :breakpoint_]
    F = matrix2[:breakpoint_, breakpoint_:]
    G = matrix2[breakpoint_:, :breakpoint_]
    H = matrix2[breakpoint_:, breakpoint_:]

    # quarters:
    # |------------|------------|
    # |            |            |
    # |    1       |      2     |
    # |------------|------------|
    # |    3       |      4     |
    # |            |            |
    # |------------|------------|

    # Strassen's 7 recursive products:

    P1 = strassen_n_by_n(A, F - H)
    P2 = strassen_n_by_n(A + B, H)
    P3 = strassen_n_by_n(C + D, E)
    P4 = strassen_n_by_n(D, G - E)
    P5 = strassen_n_by_n(A + D, E + H)
    P6 = strassen_n_by_n(B - D, G + H)
    P7 = strassen_n_by_n(A - C, E + F)

    quarter_1 = P5 + P4 - P2 + P6
    quarter_2 = P1 + P2
    quarter_3 = P3 + P4
    quarter_4 = P1 + P5 - P3 - P7

    top = np.concatenate((quarter_1, quarter_2), axis=1)        # connecting 1st with 2nd
    bottom = np.concatenate((quarter_3, quarter_4), axis=1)     # connecting 3st with 4nd
    product = np.concatenate((top, bottom), axis=0)     # connecting top n bottom

    return np.array(product)


mrix1 = squared_matrix(16, [randint(1, 100) for _ in range(256)])
mrix2 = squared_matrix(16, [randint(1, 100) for _ in range(256)])
print(strassen_n_by_n(mrix1, mrix2))
