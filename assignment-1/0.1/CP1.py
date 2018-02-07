from nest import nest
import math as ma
import numpy as np
import sympy as sp

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

# Computer problems 0.4.1a


def some_func(x):
    return (1 - sp.sec(x)) / (sp.tan(x) * sp.tan(x))


def some_other_func(x):
    return (sp.cot(x) * sp.cot(x)) * (1 - sp.sec(x))


print("Expression 10^-1:", some_func(10 ** -1), "\t", some_other_func(10 ** -1))
