frutas = ["maçã", "banana", "laranja", "melancia"]

lista = [fruta.upper() for fruta in frutas]

print(frutas)
print(lista)


inteiros = [1, 3, 4, 5, 7, 8]
quadrados = [num * num for num in inteiros]
print(inteiros)
print(quadrados)


inteiros = [1,3,4,5,7,8,9]
# pares = []
# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)
pares = [numero for numero in inteiros if numero % 2 == 0]
print(pares)