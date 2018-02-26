import numpy as np
from CP1 import gausselimLU


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


def backSubL(L):
    s = L.shape
    n = s[0]
    m = s[1]
    A = np.copy(L)
    b = A[:, m-1]
    x = [0] * n
    x[0] = b[0]/A[0, 0]
    for i in range(1, n):
        x[i] = b[i]/A[i, i]
        for j in range(i - 1, -1, -1):
            x[i] = x[i]-A[i, j] * x[j]/A[i, i]
    return x


def solve(A, S):
    L, U = gausselimLU(A)
    L = np.c_[L, S]
    x = backSubL(L)
    U = np.c_[U, x]
    y = backSub(U)
    return y


def main():
    a1 = np.array([[3.0, 1.0, 2.0], [6.0, 3.0, 4.0], [3.0, 1.0, 5.0]])
    a2 = np.array([0.0, 1.0, 3.0])
    a3 = solve(a1, a2)
    print("CP2a)")
    print(a3)

    b1 = np.array([[4.0, 2.0, 0.0], [4.0, 4.0, 2.0], [2.0, 2.0, 3.0]])
    b2 = np.array([2.0, 4.0, 6.0])
    b3 = solve(b1, b2)
    print("CP2b)")
    print(b3)
