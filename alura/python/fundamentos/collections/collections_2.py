from collections import defaultdict, Counter
usuarios_data_science = [15 ,23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# assistiram = []
# assistiram.extend(usuarios_data_science)
# print(assistiram)

assistiram = []
# retorna uma copia da lista
#assistiram = usuarios_data_science.copy()

# prolonga a lista, acrescenta ao final da lista os elementos da lista 'usuarios_data_science'
assistiram.extend(usuarios_data_science)
# prolonga a lista, acrescenta ao final da lista os elementos da lista 'usuarios_machine_learning'
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print(f'quantidade {len(assistiram)}')



# conjunto set()
print(f'conjunto {set(assistiram)}')
# cria um conjunto, o conjunto não repete 
conjunto = {4, 1, 2, 3, 5, 1, 2}
print(conjunto)

# uniao de 2 conjuntos
assistiram = set(usuarios_data_science) | set(usuarios_machine_learning)
#print(set(usuarios_data_science) | set(usuarios_machine_learning))
print(assistiram)

# intercecção de 2 conjuntos
conjunto_inter = set(usuarios_data_science) & set(usuarios_machine_learning)
print(f'intercecção de conjuntos {conjunto_inter}')


# está no usuarios_data_science e não está no usuarios_machine_leaning
conjunto_menos = set(usuarios_data_science) - set(usuarios_machine_learning)
print(f'conjuntos {conjunto_menos}')

# ou exclusivo
conjunto2 = set(usuarios_data_science) ^ set(usuarios_machine_learning)
print(f'conjuntos {conjunto2}')

# conjunto
usuarios = {1, 5, 76, 34, 52, 13, 17}
# adiciona, mas como já existe o 13 ele não adicona
usuarios.add(13)
# adiciona 765 ao conjunto
usuarios.add(765)
# congela o conjunto
usu_congela = frozenset(usuarios)
print(usuarios)
print(usu_congela)

meu_texto = 'Meu nome é Fernando e eu gosto de cachorro é muito legal eu também gosto de caminhar'
print(meu_texto)
print(meu_texto.split())
# transforma um texto em conjunto
print(set(meu_texto.split()))


# Dicionário
aparicoes = {
    'cachorro': 2,
    'gato': 1,
    'peixe': 3}

print(aparicoes)
print(aparicoes['cachorro'])
# busca a chave cavalo, se não achar retorna 0
print(aparicoes.get('cavalo', 0))

# adiciona
aparicoes['Carlos'] = 25
print(aparicoes)

# apaga uma chave
del aparicoes['peixe']

# iteração
for chave, valor in aparicoes.items():
    print(chave, valor)
for elemento in aparicoes.items():
    print(elemento)
for chave in aparicoes.keys():
    print(chave)
for valor in aparicoes.values():
    print(valor)

meu_texto = 'Bem vindo meu nome é guilherme eu gosto muito de de nomes e tenho o meu cachorro e gosto muito de gato'
# transforma o texto em minusculo
meu_texto = meu_texto.lower()

# cria um dicionario para guardar o numero de vezes que uma palavra aparece
aparicoes = {}

for palavra in meu_texto.split():
    # aparicoes.get(palavra, 0) procura a palavra, se não encontrar retorna 0
    aparicoes[palavra] = aparicoes.get(palavra, 0) + 1
print(aparicoes)



# ao pesquisar uma chave no dicionario, se não encontrar retorna 0
aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    # aparicoes.get(palavra, 0) procura a palavra, se não encontrar retorna 0
    aparicoes[palavra] = aparicoes[palavra] + 1
print(aparicoes)
# já cria o dicionário de palavras e já conta as palabras
aparicoes = Counter(meu_texto.split())
print(aparicoes)
