a = 1
b = -7.5
c = 3
from math import *
D = b**2 - 4*a*c
if D < 0:
    print("Нет корней")
elif D == 0:
    x3 = -b / (2 * a)
    print(x3)
elif D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    xmax = max(x1, x2)
    xmin = min(x1, x2)
    print(xmax,xmin)