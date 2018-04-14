import numpy as np
from sympy import Matrix, symbols, ln, E


def run_task(population_data):
    t = symbols('t', real=True)
    line_result = line(population_data, t)
    estimate = line_result.subs(t, 1980)
    actual = 4452584592
    return line_result, estimate, abs(estimate - actual)


def fill(population_data, i, j, t):
    if j == 0:
        return 1.0
    elif j == 1:
        return population_data[i][t]
    elif j == 2:
        return population_data[i][t]**2
    else:
        return population_data[i][t]**3


def line(population_data, t):
    a = Matrix(4, 2, lambda i, j: fill(population_data, i, j, 0))
    b = Matrix(4, 1, [ln(pop[1]) for pop in population_data])

    b = a.transpose() * b
    a = a.transpose() * a

    exponential = a.LUsolve(b)

    return E**exponential[0, 0] * E**(exponential[1, 0] * t)


def output():
    result = run_task(np.array([[1960, 3039585530], [1970, 3707475887], [1990, 5281653820], [2000, 6079603571]]))
    return 'Function:\t\t' + str(result[0]) \
           + "\n1980 estimate:\t" + str(result[1]) + "\t error:\t" + str(result[2])
