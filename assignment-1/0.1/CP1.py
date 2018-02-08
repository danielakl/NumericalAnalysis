from nest import nest
import math as ma
import numpy as np

# Computer problems 0.1.1


def p(x):
    return nest([1] * 51, x)


def q(x):
    return (x ** 51 - 1.0) / (x - 1.0)


x = 1.00001
horners = p(x)
equation = q(x)

diff = ma.fabs(horners - equation)
emach = np.finfo(float).eps

print("Difference of P(x) and Q(x):", diff)
print("Number of machine epsilons in difference:", diff / emach)
