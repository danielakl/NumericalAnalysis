from numpy.ma import sqrt

n1 = 3344556600
n2 = 1.2222222
sm = n1**2 + n2**2
rt = sqrt(sm)

print((n2**2)/(rt+n1), " times longer.")
