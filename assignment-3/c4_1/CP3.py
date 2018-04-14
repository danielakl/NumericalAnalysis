from sympy import Matrix, symbols, sqrt
import numpy as np


def run_task(population_data):
    line_result = line(population_data)
    parabola_result = parabola(population_data)

    t = symbols('t', real=True)

    line_result = line_result[0, 0] + line_result[1, 0] * t
    rmse_line = rmse(line_result, population_data, t)

    parabola_result = parabola_result[0, 0] + parabola_result[1, 0] * t + parabola_result[2, 0] * t**2
    rmse_parabola = rmse(parabola_result, population_data, t)

    # Actual population in 1980
    actual = 4452584592
    estimate = line_result.subs(t, 1980), parabola_result.subs(t, 1980)

    return line_result, rmse_line, parabola_result, rmse_parabola, \
           estimate[0], estimate[0] - actual, estimate[1], estimate[1] - actual


def fill(population_data, i, j, t):
    if j == 0:
        return 1.0
    elif j == 1:
        return population_data[i][t]
    elif j == 2:
        return population_data[i][t]**2
    else:
        return population_data[i][t]**3


def rmse(model, data, t):
    result = 0
    for element in data:
        result += (model.subs(t, element[0]) - element[1])**2
    return sqrt(result / len(data))


def line(population_data):
    a = Matrix(4, 2, lambda i, j: fill(population_data, i, j, 0))
    b = Matrix(4, 1, population_data[:, 1])

    b = a.transpose() * b
    a = a.transpose() * a

    return a.LUsolve(b)


def parabola(population_data):
    a = Matrix(4, 3, lambda i, j: fill(population_data, i, j, 0))
    b = Matrix(4, 1, population_data[:, 1])

    b = a.transpose() * b
    a = a.transpose() * a

    return a.LUsolve(b)


def output():
    result = run_task(np.array([[1960, 3039585530], [1970, 3707475887], [1990, 5281653820], [2000, 6079603571]]))
    return "Line:\t\t" + str(result[0]) \
           + "\nRMSE line:\t" + str(result[1]) \
           + "\nParabola:\t" + str(result[2]) \
           + "\nRMSE parabola:\t" + str(result[3]) \
           + "\n1980 line:\t\t" + str(result[4]) + "\terror:\t" + str(result[5]) \
           + "\n1980 parabola:\t" + str(result[6]) + "\terror:\t" + str(result[7])
