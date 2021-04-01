import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


mydata = pd.read_csv("rainfall-1.csv")

x = mydata["Monthly Precipitation Total (millimetres)"].values
y = mydata["Month"].values


for month in range(1,13):
    highest = 0
    lowest = np.Infinity
    s=0
    count = 0
    for j in range(0,len(y)):
        if y[j] == month:
            s += x[j]
            count += 1
            if x[j] > highest:
                highest = x[j]
            if x[j] < lowest:
                lowest = x[j]

    mean = s/count

    print('month:', month, highest, lowest, mean)
