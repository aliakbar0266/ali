from random import randint
import numpy as np


# Generating retrivable shuffle Map
def Perm_Seed(Seed, Array_Len):
    np.random.seed(Seed)
    Map = np.random.permutation(Array_Len)
    return Map


# ALICE AND BOB for Generating SEED
def choose_prime_number(lower, upper):
    import time
    from random import randrange
    start = time.time()
    prime = []
    tim = []
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
                tim.append((time.time() - start))
    leng = len(prime)
    rnd = randrange(0, leng - 1)
    pr = prime[rnd]
    return pr


# Comparing generated shuffled array
def comparison(a, b):
    flag = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            flag = 0
        else:
            flag = 1

    if flag == 0:
        print("arrays are the same")
    elif flag == 1:
        print("arrays are not the same")

    return flag


# Shuffling arrays using Map
def Shuffle_Array(Map, Array):
    Ret_Array = Array
    l = len(Map)
    Sh_Ar = np.zeros(l)
    for i in range(l):
        Sh_Ar[i] = Array[Map[i]]
    return Sh_Ar


class SeedRandomGenerator(object):
    # get seed value
    def seed(self, a=3):
        """Assigning a value to seed"""
        self.seed_Value = a

    def random(self):
        """Generating a random number using Defined Equation and seed value"""
        self.seed_Value = (self.seed_Value * 21) % 2587
        return self.seed_Value


"""Generating arrays of Array_Len random values"""

# Generating Seed for Generating Map
# Seed can also be generated through Alice and Bob Req. Sharede seceret key can be taken as a Seed
print(
    "input required values for prime generator function in order to generate seed (bob and alice's shared secret key)")
lower = int(input("input the lower value of interval :   "))
upper = int(input("input the upper value of interval:    "))
# Publicly shared values,  p and  g
p = choose_prime_number(lower, upper)
g = choose_prime_number(lower, upper)
# Get Private keys, a is Alice's Private key, b is Bob's Private key
a = int(input("input a value as  Alice's Private key : "))
b = int(input("input a value as Bob's Private key : "))
# Alice and Bob compute public values
# Alice Sends Bob x = g^a mod p
x = (g ** a) % p
print("\nAlice Sends Over Public Chanel: ", x)
# Bob Sends Alice y = g^b mod p
y = (g ** b) % p
print("Bob Sends Over Public Chanel: ", y)
# Alice and Bob exchange public numbers and then compute symmetric keys
Ka = (y ** a) % p
Kb = (x ** b) % p
print("shared secret key", Ka)
Array_Len = 10
Seed = Ka
Num_Arr = 5
Gen = np.zeros((Num_Arr, Array_Len))

Obj = SeedRandomGenerator()
seed = Obj.seed
random = Obj.random

for cont in range(Num_Arr):
    seed(5)
    g = [random() for _ in range(Array_Len)]
    Gen[cont] = g
    # print(g)

# Generating Map
Map = Perm_Seed(Seed, Array_Len)
index = randint(0, Num_Arr - 1)
Array = Gen[index]
Shuffled_Ar = Shuffle_Array(Map, Array)

print("Map to Shuffle the array is: ", Map)
print("Original Array Is : ", Array)
print("Shuffled Array Is : ", Shuffled_Ar)

## COmparing Generated arrays
print("Comparing to shuffled array with the same seed")

fa = Shuffle_Array(Map, Array)
print("The first shuffled array is: ", fa)
sa = Shuffle_Array(Map, Array)
print("The second shuffled array is: ", sa)

print(comparison(fa, sa))