# Defining a generator to get a value called seed to generate same random numbers in each run
import random
from random import randrange
import numpy as np


class SeedRandomGenerator(object):
    # get seed value
    def seed(self, a=3):
        """Assigning a value to seed"""
        self.seed_Value = a

    def random(self):
        """Generating a random number using Defined Equation and seed value"""
        self.seed_Value = (self.seed_Value * 21) % 2587
        return self.seed_Value


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


Obj = SeedRandomGenerator()
seed = Obj.seed
random = Obj.random
"""Generating arrays of 200 random values"""
Gen = np.zeros((5, 200))
for cont in range(5):
    seed()
    g = [random() for _ in range(200)]
    Gen[cont] = g
    print(g)

fa = randrange(1, 5)
sa = randrange(1, 5)
if fa == sa:
    while fa == sa:
        sa = randrange(1, 200)

print(comparison(Gen[(fa)], Gen[(sa)]))
