# agora o peso e o bias são listas 

import math as m
import random

def S(x, w, b):
    for i in range(len(x)):
        result =  (x[i] * w[i])            # soma ponderada
    result = result + b
    return result

def sigmoid(S):
    return 1 / ( 1 + m.e ** (-S))  # função de ativação

# >> [0, 0, 1]

t = 1.00                                  # target
lr = 0.05                                 # learning rate
x = [2, 4.1, 0.3, 1.6, 2.3]               # input 
w = [0.42462815628117523, 0.17530149531094286, 0.7748712199598842, 0.4016443995021405, 0.48989714383729704]
# w = [random.random() for i in range(5)]   # peso 
b = random.random()                       # viés

epochs = 100 

for i in range(100):
    sum = S(x , w, b)                   # soma ponderada
    y = sigmoid(sum)                    # sigmoid

    error = 0.5 * pow((t - y), 2)       # função de erro 
    for i in range(len(x)):
        bias =  (y - t) * y * (1 - y) * x[i]   # derivada do Erro em relação ao bias
        weight = (y - t) * y * (1 - y)      # derivada do Erro em relação ao viés

    w[i] = w[i] - lr * weight
    b = b - lr * bias
    print(sigmoid(S(x, w, b)), error)
    pass