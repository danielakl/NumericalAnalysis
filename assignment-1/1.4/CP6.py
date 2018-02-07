# Volume of cone: V_c = pi*r^2*h/3
# Volume of hemisphere: V_h = 2*pi*r^3/3
# Total volume: V_c + V_h = pi*r^2*h/3+2*pi*r^3/3
from numpy.core.umath import pi


V = 60


def func(r):
    return r - ((2 * pi * r ** 3) / 3 + (10 * pi * r ** 2) / 3 - V) / (2 * pi / 3 * r * (3 * r + 10))


n1 = 100
n2 = 0
while n1 != n2:
    n2 = n1
    n1 = func(n1)
print("n:", n1)
