# listas
idades = [20, 39, 18, 27, 19]
for idade in idades:
    print(idade, idade  + 1)
print(idades)

# list comprehension
idade_ano_que_vem = [(idade + 1) for idade in idades]
print(idade_ano_que_vem)

# list comprehension
print([idade for idade in idades if idade > 21])

