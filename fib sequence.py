import matplotlib.pyplot as plt
import numpy as np


N = int(input("How money numbers would you like to count: "))
fib = np.zeros(N)

fib[0] = 0
fib[1] = 1

for i in range(2,N,1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib)