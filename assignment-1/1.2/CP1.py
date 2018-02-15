# (a) x^3 =2x +2 (b) e^x +x = 7 (c) e^x +sin(x) = 4.
from numpy.core.umath import e, sin, cos


def func1(x):
    return x - (x ** 3 - 2 * x - 2) / (3 * x ** 2 - 2)


def func2(x):
    return x - (e ** x + x - 7) / (e ** x + 1)


def func3(x):
    return x - (e ** x + sin(x) - 4) / (e ** x + cos(x))


a1 = 10
a2 = 0
i1 = 0
while abs(a1 - a2) > 0.000000005:
    i1 += 1
    a2 = a1
    a1 = func1(a1)
print("a:", a1, i1)

b1 = 10
b2 = 0
i2 = 0
while abs(b1 - b2) > 0.000000005:
    i2 += 1
    b2 = b1
    b1 = func2(b1)
print("b:", b1, i2)

c1 = 10
c2 = 0
i3 = 0
while abs(c1 - c2) > 0.000000005:
    i3 += 1
    c2 = c1
    c1 = func3(c1)
print("c:", c1, i3)
