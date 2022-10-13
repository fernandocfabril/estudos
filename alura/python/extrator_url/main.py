# coding: utf-8

# base da URL = https://bytebank.com/cambio
# ? indica que serão passado parametros na URL
# parametros da URL = moedaOrigem=real&moedaDestino=dolar&quantidade=100
# o & é utilizado para separar os parametros
#url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
url = '                  '

# sanitização/limpeza da URL
url = url.strip()   # remove os espaços em brando no inicio e no fim da url

#print(f'url {url}')

# validação da URL
if url == '':
    raise ValueError('A URL está vazia')



# url.find('?') acha a posição do caracter '?'
indice_interrogacao = url.find('?')
# pega da posição 0 até a posição do caracter "?"
url_base = url[0:indice_interrogacao]
print(f'url_base {url_base}')

# url.find('?') acha a posição do caracter '?'
# pega da posição do caracter "?" + 1 e vai até o final
url_parametros = url[indice_interrogacao+1:]
print(f'url_parametros {url_parametros}')

# buscar o valor do parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(f'Valor {valor}')
