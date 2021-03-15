import matplotlib.pyplot as plt
import numpy as np
import math


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

D = (b**2) - (4 * a * c)

if D < 0:
    N = 0
    print("There are no roots")
elif D == 0:
    N = 1
    x1 = -b/(2*a)
    print("N =",N)
elif D > 0:
    N = 2
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b - sqrt(D)) / (2*a)




