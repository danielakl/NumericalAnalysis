from numpy.ma import tan
from sympy import sec


# Breaks down as x approaches 0
def func(x):
    return (1 - sec(x)) / (tan(x) ** 2)


# Breaks down as x approaches pi
def sup(x):
    return -1 / (sec(x) + 1)


print("X", "\t", "Difference")
for i in range(1, 15, 1):
    r = 10 ** -i
    res1 = func(r)
    res2 = sup(r)
    diff = res1 - res2
    print(r, "\t", diff)
