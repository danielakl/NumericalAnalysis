import numpy as np


def gausselim(A):
    s = A.shape
    n = s[0]
    m = s[1]
    G = np.copy(A)

    for j in range(0, n-1):
        for i in range(j+1, n):
            mult = (G[i, j]/G[j, j])
            for k in range(j, m):
                G[i, k] = G[i, k]-G[j, k] * mult
    return G


def backSub(Ain):
    s = Ain.shape
    n = s[0]
    m = s[1]
    A = np.copy(Ain)
    b = A[:, m-1]
    x = [0] * n
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = b[i] / A[i, i]
        for j in range(i+1, n):
            x[i] = x[i] - A[i, j] * x[j]/A[i, i]
    return x


def cp2c21(n):
    A = 1. / (np.arange(1, n + 1) + np.arange(0, n)[:, np.newaxis])
    A = np.c_[A, np.ones(n)]
    B = gausselim(A)
    S = backSub(B)
    return(S)


A = np.array([
    [2.0, -2.0, -1.0, -2.0],
    [4.0, 1.0, -2.0, 1.0],
    [-2.0, 1.0, -1.0, -3.0]
])
B = np.array([
    [1.0, 2.0, -1.0, 2],
    [0, 3.0, 1.0, 4],
    [2.0, -1.0, 1.0, 2]
])
C = np.array([
    [2.0, 1.0, -4.0, -7],
    [1, -1.0, 1.0, -2],
    [-1.0, 3.0, -2.0, 6]
])

print("CP1a)")
print(gausselim(A))
print(backSub(gausselim(A)))
print("CP1b)")
print(gausselim(B))
print(backSub(gausselim(B)))
print("CP1c)")
print(gausselim(C))
print(backSub(gausselim(C)))

print
print("CP2a)")
print(cp2c21(2))
print("CP2b)")
print(cp2c21(5))
print("CP2c)")
print(cp2c21(10))
