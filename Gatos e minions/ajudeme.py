import math as m
import random as rd

def S(x, w, b):
    somaTotal = 0
    for i in range (len(x)):
        somaTotal += x[i] * w[i]
    return somaTotal + b

def sigmoid(s):
    return 1/((1 + m.exp(-s)))    

W = [rd.random() for i in range (10)]
B = rd.random()
X = [3.0, 4.5, 6.0, 9.0, 8.0, 10.0, 2.4, 5.4, 5.3, 8.9]
t = 0.80
epochs = 1000
lr = 0.05

for i in range(epochs):
    y = sigmoid(S(X, W, B))
    tian = (y-t) * y * (1-y)
    B = B - lr * tian
    for j in range(len(X)):
        chris = (y-t) * y * (1-y) * X[j]
        
        W[j] = W[j] - lr * chris
        
    print(f"Epoca: {i}| Saida: {sigmoid(S(X, W, B))} | Erro: {y}")

