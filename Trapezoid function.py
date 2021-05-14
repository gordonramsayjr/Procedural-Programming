import numpy as np

def v(x):
    return 3*np.sin(0.1*x)

def trapezoidal(f,a,b,n):
    h = (b-a)/n
    f_sum = 0
    for i in range(1,n,1):
        x = a + i * h
        f_sum += f(x)
    return h*(0.5*f(a) + f_sum + 0.5*f(b))

n = 10
trap = trapezoidal(v, 0, (np.pi/4), n)

print("Trapezoidal, {} sub-intervals: {:.8f}".format(n,trap))

