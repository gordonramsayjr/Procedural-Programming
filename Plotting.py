import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0,np.pi,500)
y = 2*np.sin(5*t+np.pi)

plt.plot(t,y)
plt.title("Oscillation One Vs. Time")
plt.show()