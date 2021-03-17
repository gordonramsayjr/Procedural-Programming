import matplotlib.pyplot as plt               # import matplotlib and numpy libraries
import numpy as np


t = np.linspace(0,np.pi,500)                  # defines t as an array that has 500 values between 0 and pi.
y = 2*np.sin(5*t+np.pi)                       # equation to get y

plt.plot(t,y)                                 # plots all t and y elements
plt.title("Oscillation One Vs. Time")         # defines graph title
plt.show()                                    # shows graph
