import math as m
import random

def S(x, w, b):
    return (x * w ) + b # soma ponderada

def sigmoid(S):
    return 1 / (1+ m.e ** (-S)) # função de ativação

# >> [0, 0, 1]

lr = 0.05            # learning rate
t = 1.00             # target
x = 1.6              # input 
w = random.random()  # peso 
b = random.random()  # viés

epochs = 100 

for i in range(100):

    soma = S(x , w, b)   # soma ponderada
    y = sigmoid(soma)    # sigmoid

    error = 0.5 * pow((t - y), 2)  # função de erro 

    bias =  (y - t) * y * (1 - y) * x # derivada do Erro em relação ao bias
    weight = (y - t) * y * (1 - y)    # derivada do Erro em relação ao viés

    w = w - lr * weight
    b = b - lr * bias

    output = sigmoid(S(x, w, b))    
    print(f"Época: {i} | Saída: {output} | Erro: {error}")
    pass