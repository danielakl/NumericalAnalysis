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


def main():
    print("CP1a)")
    a = gausselimLU(np.array([[3.0, 1.0, 2.0], [6.0, 3.0, 4.0], [3.0, 1.0, 5.0]]))
    print("L:")
    print(a[0])
    print("U:")
    print(a[1])

    print
    print("CP1b)")
    b = gausselimLU(np.array([[4.0, 2.0, 0.0], [4.0, 4.0, 2.0], [2.0, 2.0, 3.0]]))
    print("L:")
    print(b[0])
    print("U:")
    print(b[1])

    print
    print("CP1c)")
    c = gausselimLU(np.array([[1.0, -1.0, 1.0, 2.0], [0.0, 2.0, 1.0, 0.0], [1.0, 3.0, 4.0, 4.0], [0.0, 2.0, 1.0, -1.0]]))
    print("L:")
    print(c[0])
    print("U:")
    print(c[1])
