import numpy as np


def next(S, i):
    if i == 0:
        return (S[i+1]+2)/3
    if i == len(S)-1:
        return (S[i-1]+2)/3
    return (S[i+1]+S[i-1]+1)/3


def main(n):
    # A = np.array([[0.0] * n for _ in range(n)])
    # for i in range(0, n):
    #     A[i, i] = 3
    # for i in range(1, n):
    #     A[i-1, i] = -1
    #     A[i, i-1] = -1
    S = [1.0]*n
    S[0] = 2.0
    S[len(S)-1] = 2.0
    c = 0
    solved = False
    while not solved:
        c += 1
        sc = 0  # solve count
        for i in range(0, n):
            t = next(S, i)
            if abs(S[i]-1) < 0.0000005:
                sc += 1
            S[i] = t
        if sc == n:
            solved = True
    m = 0
    for i in range(0, n):
        t = abs(S[i]-1)
        if t > m:
            m = t
    return c, m


print('100:', main(100))
print('100000:', main(100000))
