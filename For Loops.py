import numpy as np


sequence = np.zeros(10)
sum = 0
sum23 = 0
for i in range(0,10,1):
    sequence[i] = (0.2*sequence[i-1]) + (1.2*sequence[i-2])

    sequence[0] = 1
    sequence[1] = 1.5

    print(sequence[i])

    if 2 <= sequence[i] <= 3:
        sum23 += sequence[i]

    sum += sequence[i]

print(sum)
print(sum23)