import numpy as np

# 10**−20*x**1 +   x**2 = 1
#         x**1 + 2*x**2 = 4

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


A2 = np.array([[10**-20, 1, 1], [1, 2, 4]])

G2 = backSub(gausselim(A2))

print(G2)  # [0.0, 1.0]

A3 = np.array([[1, 2, 4], [10**-20, 1, 1]])

G3 = backSub(gausselim(A3))

print(G3)  # [2.0, 1.0]
