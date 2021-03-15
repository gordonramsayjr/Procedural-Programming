import math


for x in range(100):
    if x % 5 == 0 and x % 3 == 0:
        print("Bingo!")
    elif x % 3 == 0:
        print(x,"Is divisible by 3!")

    elif x % 5 == 0:
        print(x,"Is divisible by 5!")


    print(x)