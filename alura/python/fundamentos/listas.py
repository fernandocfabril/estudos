idades = [15, 87, 32, 65, 56, 32, 49, 37]

# ordenação
print(f'antes da ordenação {idades}')
#sorted(idades)
print(f' ordenação da lista{sorted(idades)}')
#reversed(idades)
print(f'reversão da lista {list(reversed(idades))}')
print(f'ordem invertida da lista {sorted(idades, reverse=True)}')

# ordenação da lista e altera a propria lista
print(f'\nantes da ordenação {idades}')
idades.sort()
print(f'depois da ordenação {idades}')

nomes = ['Guilherme', 'Daniela', 'Paulo', 'Antonio']
print(f'Ordenar lista com nomes {nomes}')
print(f'Ordenar lista com nomes {sorted(nomes)}')