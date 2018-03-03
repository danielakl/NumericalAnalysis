import numpy as np
from GaussLU import gausselimLU


def main():
    print("CP1a)")
    a = gausselimLU(np.array([[3.0, 1.0, 2.0], [6.0, 3.0, 4.0], [3.0, 1.0, 5.0]]))
    print("L:")
    print(a[0])
    print("U:")
    print(a[1])

    print("CP1b)")
    b = gausselimLU(np.array([[4.0, 2.0, 0.0], [4.0, 4.0, 2.0], [2.0, 2.0, 3.0]]))
    print("L:")
    print(b[0])
    print("U:")
    print(b[1])

    print("CP1c)")
    c = gausselimLU(np.array([[1.0, -1.0, 1.0, 2.0], [0.0, 2.0, 1.0, 0.0], [1.0, 3.0, 4.0, 4.0], [0.0, 2.0, 1.0, -1.0]]))
    print("L:")
    print(c[0])
    print("U:")
    print(c[1])


main()
