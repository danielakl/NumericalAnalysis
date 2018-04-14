from sympy import symbols, Matrix, sqrt


def run_task(points, radii):
    variables = x, y = symbols('x y', real=True)
    functions = sqrt((x - points[0][0])**2 + (y - points[0][1])**2) - radii[0], \
                sqrt((x - points[1][0])**2 + (y - points[1][1])**2) - radii[1], \
                sqrt((x - points[2][0])**2 + (y - points[2][1])**2) - radii[2]

    xk = Matrix(2, 1, lambda _, __: 0.0)
    dr = Matrix(3, 2, lambda i, j: (variables[j] - points[i][j]) / (functions[i] + radii[i]))
    r = Matrix(3, 1, lambda i, _: functions[i])

    for k in range(20):
        a = dr.subs([(x, xk[0]), (y, xk[1])]).evalf()
        rk = r.subs([(x, xk[0]), (y, xk[1])]).evalf()
        vk = (a.transpose() * a).LUsolve(-a.transpose() * rk)
        xk += vk

    return xk


def output():
    result = run_task([[0, 1], [1, 1], [0, -1]], [1, 1, 1])
    return '(x, y) = (' + str(result[0]) + ', ' + str(result[1]) + ')'
