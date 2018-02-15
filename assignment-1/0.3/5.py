from math import floor

from numpy.random import random

print((1+(2**-51+2**-53))-1)

print((1+(2**-51+2**-52+2**-53))-1)

r1 = floor(random() * 1001)
r2 = floor(random() * 1001)
r3 = floor(random() * 1001)
c = 0

while r1 + r2 + r3 != 3000:
    r1 = floor(random() * 1001)
    r2 = floor(random() * 1001)
    r3 = floor(random() * 1001)
    c += 1
print(c)
