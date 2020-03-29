
# Finding Prime numbers between given intervals


import time
import matplotlib.pyplot as plt
import numpy as np


LowerBound=int(input("input the lower value:   "))
UpperBound= int(input("input the upper value:    "))

start=time.time()

prime=[]
tim=[]
for x in range(LowerBound, UpperBound + 1):
   # all prime numbers are greater than 1
   if x > 1:
       for i in range(2, x):
           if (x % i) == 0:
               break
       else:
           prime.append(x)
           tim.append((time.time()-start))


print("The generated prime numbers in given interval are:", prime)



# ploting the prime values and according to their discovering time
plt.plot(tim,prime)
plt.plot(tim,prime)
plt.ylabel('Prime')
plt.xlabel('Time')
plt.show()