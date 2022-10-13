# Modulo de Regular Expression -- RegEx
import re 

endereco = 'Rua Topazio, 1805, Jardim Paris II, 87083-373, Maringa-Paraná'

print(f'Endereco: {endereco}')

# padrão do cep
# 5 digitos + hifen (opcional) + 3 digitos

# [0-9]{5} -> numeros de 0 a 9 cinco vezes (87083)
# [-]{0,1} -> hifen pode aparecer 1 vez ou nenhuma (-)
# [0-9]{3} -> numeros de 0 a 9 tres vezes (373)
padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
# buscar um padrao dentro de uma string
busca = padrao.search(endereco) # retorna Match
# se não encontrar, retorna None
if busca:
    cep = busca.group()
    print(f'Cep: {cep}')
