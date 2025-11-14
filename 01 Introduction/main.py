import math as m
import random

def S(x, w, b):
    return (x * w ) + b

def sigmoid(S):
    1/((1+ m.e) ** -S)

# >> [0, 0, 1]

t = 1.00
x = 1.6
w = random.random()
b = random.random()

epochs = 100 

for i in range(100):
    print(sigmoid(S(x, w, b)))
    pass