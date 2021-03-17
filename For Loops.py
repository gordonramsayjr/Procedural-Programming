import numpy as np              # imports numpy as shortened np


sequence = np.zeros(10)         # defines sequence as an array of 10 zeros.

sum1 = 0                        # defines sum1 and sum2  as 0 for later use 
sum2 = 0

for i in range(0,10,1):         # initialises for loop in the range of 0-10 values, wth 1 space between.
    
    sequence[i] = (0.2*sequence[i-1]) + (1.2*sequence[i-2])         # equation stating that the current interation 
                                                                    # is equal to 0.2 * the previous iteration + 1.2 * the 
                                                                    # iteration two before the current

    sequence[0] = 1                      # forces the first and second elements of the sequence 
    sequence[1] = 1.5                    # array to be 1 and 1.5

    print(sequence[i])                   # prints the current iteration's calculated value
    

    if 2 <= sequence[i] <= 3:            # if statement declaring if the current interation is
        sum2 += sequence[i]              # between 2 and 3 then add those interations together

    sum1 += sequence[i]                  # adds the current iteration to the total sum of all iterations

print(sum1)                              # prints both sums
print(sum23)
