from numpy.ma import sqrt

n1 = 3344556600
n2 = 1.2222222
sm = n1**2 + n2**2
rt = sqrt(sm)

print(rt-n1)
# rt-n1 = (rt-n1)*(rt+n1) / (rt+n1) = (sm-n1^2)/(rt+n1) = (n2^2)/(rt+n1)
print((n2**2)/(rt+n1))
