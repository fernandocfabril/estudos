# -*- coding: utf-8 -*-

# Newton-Raphson para raiz quadrada
# Encontrar x tal que x**2 - 24 está a menos de epsilon de 0

epsilon = 0.01
k = 24.0
estimativa = k /2.0
n = 0
while abs(estimativa * estimativa - k) >= epsilon:
    estimativa = estimativa - (((estimativa ** 2) - k) / (2 * estimativa))
    n += 1


print(f'A raiz quadrada de {k} é aproximadamente {estimativa} em {n} iterações')
