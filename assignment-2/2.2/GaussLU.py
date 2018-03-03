import numpy as np


def gausselimLU(A):
    s = A.shape
    n = s[0]
    m = s[1]
    U = np.copy(A)
    L = np.array([[0.0] * n for _ in range(n)])

    for m in range(0, n):
        L[m, m] = 1

    for j in range(0, n-1):
        for i in range(j+1, n):
            mult = (U[i, j]/U[j, j])
            L[i, j] = mult
            for k in range(j, m+1):
                U[i, k] = U[i, k]-U[j, k] * mult
    return L, U