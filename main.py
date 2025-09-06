from math import *
a = int(input("a: "))
z1 = cos(a) + sin(a) + cos(3*a) + sin(3 * a)
b = round(z1, 3)
print(b)

z2 = 2 * 2**0.5 * cos(a) * sin(pi / 4 + 2 * a)
print(round(z2, 3))
