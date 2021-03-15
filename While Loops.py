import numpy as np

s = np.zeros(10)
v = 0
sum = 0
sum23 = 0

while v < len(s):
    s[0] = 1.0
    s[v] = 0.8*(s[v-1]) + 1

    print(s[v])

    sum += s[v]

    if 2 <= s[v] <= 3:
        sum23 += s[v]

    v += 1

print(sum)
print(sum23)


