# agora o peso e o bias são listas 

import math as m
import random

def S(x, w, b):
    result = 0
    for i in range(len(x)):
        result =  (x[i] * w[i])            # soma ponderada 
    return result + b

def sigmoid(S):
    return 1 / ( 1 + m.e ** (-S))  # função de ativação

# >> [0, 0, 1]

t = 1.00                                  # target
lr = 0.05                                 # learning rate
x = [2, 4.1, 0.3, 1.6, 2.3]               # input 
w = [0.42462815628117523, 0.17530149531094286, 0.7748712199598842, 0.4016443995021405, 0.48989714383729704]
b = random.random()                       # viés

epochs = 100 

for i in range(epochs):
    sum = S(x , w, b)                   # soma ponderada
    y = sigmoid(sum)                    # sigmoid

    error = 0.5 * (t - y)** 2       # função de erro 

    for j in range(len(x)):
        bias =  (y - t) * y * (1 - y) * x[j]   # derivada do Erro em relação ao bias
        weight = (y - t) * y * (1 - y)      # derivada do Erro em relação ao viés

    w[j] = w[j] - lr * weight
    b = b - lr * bias

    output = sigmoid(S(x, w, b))

    print(f"Época: {i} | Saída: {output} | Erro: {error}")
    pass