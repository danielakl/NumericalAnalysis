from numpy.ma import tan, floor
from numpy.random import random
from sympy import sec


# Breaks down as x approaches 0
def func(x):
    return (1 - sec(x)) / (tan(x) ** 2)


# Breaks down as x approaches pi
def sup(x):
    return -1 / (sec(x) + 1)


for i in range(1, 15, 1):
    r = 10 ** -i
    res1 = func(r)
    res2 = sup(r)
    diff = res1 - res2
    print(r, "\t", res1, "\t", res2, "\t", diff)
    # print("x:", r, "1:", res1, ", 2:", res2, ", diff:", diff)
