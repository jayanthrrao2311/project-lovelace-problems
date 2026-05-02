from math import sqrt
def temperature_statistics(T):
    N = len(T)
    temp = 0
    for i in T:
        temp += i
    mean = temp / N
    temp1  = 0
    for i in T:
        temp1 += (i - mean) ** 2 
       
    std = sqrt(temp1 / N)
   
    return mean, std