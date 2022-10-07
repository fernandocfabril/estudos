frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja escolher? ')

# remove os espaços em branco no inicio e final
fruta_pedida.strip()

# primeira letra maiscula
fruta_pedida = fruta_pedida.capitalize()

if (fruta_pedida in frutas):
    print(f'Sim, temos a fruta {fruta_pedida}.')

else:
    print(f'Não temos a fruta {fruta_pedida}.', end='\n')
    print(f'Temos as seguintes furtas: \n\t {frutas}')

