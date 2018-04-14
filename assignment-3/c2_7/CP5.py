from sympy import symbols, diff, Matrix


def run_task(first_vector, second_vector, sphere_props, iterations):
    # Defining variables and functions.
    variables = x, y, z = symbols('x y z', real=True)
    functions = f1, f2, f3 = \
        (x - sphere_props[0][0]) ** 2 + (y - sphere_props[0][1]) ** 2 + (z - sphere_props[0][2]) ** 2 - sphere_props[0][3] ** 2, \
        (x - sphere_props[1][0]) ** 2 + (y - sphere_props[1][1]) ** 2 + (z - sphere_props[1][2]) ** 2 - sphere_props[1][3] ** 2, \
        (x - sphere_props[2][0]) ** 2 + (y - sphere_props[2][1]) ** 2 + (z - sphere_props[2][2]) ** 2 - sphere_props[2][3] ** 2

    # Defining matrices to use.
    DF = Matrix(3, 3, lambda i, j: diff(functions[i], variables[j]))
    F = Matrix([f1, f2, f3])
    X = Matrix(first_vector)

    # Finding first point
    # Running Multivariate Newton’s Method
    for _ in range(iterations):
        X += DF.LUsolve(-F).subs([(x, X[0, 0]), (y, X[1, 0]), (z, X[2, 0])])

    point1 = X, F.subs([(x, X[0, 0]), (y, X[1, 0]), (z, X[2, 0])])

    # Finding second point
    # Running Multivariate Newton’s Method
    X = Matrix(second_vector)
    for _ in range(iterations):
        X += DF.LUsolve(-F).subs([(x, X[0, 0]), (y, X[1, 0]), (z, X[2, 0])])

    point2 = X, F.subs([(x, X[0, 0]), (y, X[1, 0]), (z, X[2, 0])])

    return point1[0], point1[1], point2[0], point2[1]


def output():
    result = run_task([0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [[1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]], 20)
    x_point1_radius1 = result[0]
    error_point1_radius1 = result[1]
    x_point2_radius1 = result[2]
    error_point2_radius1 = result[3]

    result = run_task([10.0, 10.0, 10.0], [-10.0, -10.0, -10.0], [[1, -2, 0, 5], [-2, 2, -1, 5], [4, -2, 3, 5]], 20)
    x_point1_radius5 = result[0]
    error_point1_radius5 = result[1]
    x_point2_radius5 = result[2]
    error_point2_radius5 = result[3]

    return "Each sphere have radius of 1\nFirst point:\nResult:\t" + str([_ for _ in x_point1_radius1]) \
           + "\nError:\t" + str([_ for _ in error_point1_radius1]) \
           + "\n\nSecond point:\nResult:\t" + str([_ for _ in x_point2_radius1]) \
           + "\nError:\t" + str([_ for _ in error_point2_radius1]) \
           + "\n\nEach sphere have radius of 5\nFirst point:\nResult:\t" + str([_ for _ in x_point1_radius5]) \
           + "\nError:\t" + str([_ for _ in error_point1_radius5]) \
           + "\n\nSecond point:\nResult:\t" + str([_ for _ in x_point2_radius5]) \
           + "\nError:\t" + str([_ for _ in error_point2_radius5])
