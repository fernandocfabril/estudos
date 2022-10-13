import extrator_url

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

valor_dolar = 5.50

extrator = extrator_url.ExtratorURL(url)

moeda_origem = extrator.get_url_parametros_valor('moedaOrigem').upper()
moeda_destino = extrator.get_url_parametros_valor('moedaDestino').upper()
quantidade = float(extrator.get_url_parametros_valor('quantidade'))


if moeda_origem not in ['REAL', 'DOLAR'] or moeda_destino not in ['REAL', 'DOLAR']:
    valor = 0
    print(f'A conversão de {moeda_origem} para {moeda_destino} não está disponível')
else:
    if moeda_origem == 'REAL' and moeda_destino == 'DOLAR':
        valor = quantidade / valor_dolar
    elif moeda_origem == 'DOLAR' and moeda_destino == 'REAL':
        valor = quantidade * valor_dolar
    elif moeda_origem == moeda_destino:
        valor = quantidade
    print(f'A conversão do valor {quantidade:.2f} de {moeda_origem} para {moeda_destino} é {valor:.2f}')
