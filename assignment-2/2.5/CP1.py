import numpy as np
import scipy as sp
from scipy.sparse import spdiags


def jacobi(n):
    A, B = make_matrix(n)
    D = A.diagonal()
    e = sp.ones(n)
    R = spdiags([-e, -e], [-1, 1], n, n)
    c = 0
    x = np.zeros(n)
    x0 = np.zeros(n)

    while True:
        c += 1
        x = (B - (R * x)) / D
        correct = 0
        for j in range(len(x)):
            if abs(x[j]-1) < 0.0000005:
                correct += 1
        if correct == n:
            dif = np.zeros(n)
            for k in range(n):
                dif[k] = abs(x0[k] - x[k])
            be = 1 - min(dif)
            return c, be


def make_matrix(n):
    e = sp.ones(n)
    A = spdiags([-e, 3*e, -e], [-1, 0, 1], n, n)

    B = np.zeros(n)
    B[0] = 2
    B[n-1] = 2
    B[1: n-1] = 1
    return A, B


# print('10:', jacobi(10))
print('100:', jacobi(100))
print('100000:', jacobi(100000))
