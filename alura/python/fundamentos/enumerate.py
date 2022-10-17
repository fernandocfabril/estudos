
idades = [15, 87, 32, 65, 56, 32, 49, 37]

for valor in enumerate(idades):
    print(valor)

for i, valor in enumerate(idades):
    print(i, valor)


lista = list(enumerate(idades))
print(lista)

usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Paulo', 39, 1979)
]

for usuario in usuarios:
    print(usuario)

# desempacotamento
for nome, idade, nascimento in usuarios:
    print(nome, idade, nascimento)

# desempacotamento ignorando os outros elementos e considerando comente o nome
for nome, _, _ in usuarios:
    print(nome)

for nome, *args in usuarios:
    print(nome)