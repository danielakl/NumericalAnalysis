from sympy import symbols, diff, Matrix


def run_task(iterations):
    """
    Run Newton's method on a system.
    :param iterations: The number of iterations to run Newton's Method.
    :return: The result of Newton's Method and the error.
    """
    # Defining variables and functions.
    variables = u, v = symbols('u v', real=True)
    functions = f1, f2 = u**3 - v**3 + u, u**2 + v**2 - 1

    # Defining matrices to use.
    DF = Matrix(2, 2, lambda i, j: diff(functions[i], variables[j]))
    F = Matrix([f1, f2])
    X = Matrix([1.0, 1.0])

    # Running Newton's Method
    for _ in range(iterations):
        X += DF.LUsolve(-F).subs([(u, X[0, 0]), (v, X[1, 0])])

    return X, F.subs([(u, X[0, 0]), (v, X[1, 0])])


def output():
    result = run_task(20)
    X = result[0]
    error = result[1]
    return "Result:\t" + str([_ for _ in X]) + "\nError:\t" + str([_ for _ in error])
