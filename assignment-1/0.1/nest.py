# Computer problems 0.1.1

# Evaluates polynomial from nested form using Horner's method.
# c - is an array of coefficients.
# x - is the point to evaluate.
# b - is an optional array of null points.


def nest(c, x, b=None):
    d = len(c) - 1
    if b is None:
        b = [0] * d
    y = c[d]
    for i in range(d - 1, -1, -1):
        y *= (x - b[i])
        y += c[i]
    return y
