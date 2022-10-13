# Modulo de Regular Expression -- RegEx
import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        # verifica se url é do tipo string
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        # se self.url for vazia retorna False
        if not self.url:
            raise ValueError('A URL está vazia!')

        # validar com RegEx
        # define o padrão
        #   (http(s)?://)? -> pode começar com 'http://' ou 'https://'
        #   (www.)? -> pode conter ou não 'www.'
        #   (bytebank.com(.br)?) -> deve conter 'bytebank.com' ou 'bytebank.com.br'
        #   (/cambio) -> deve conter '/cambio'
        # quando colocamos algum texto entre () esse texto deve existir
        # quando colocamos algum texto entre [] esse texto pode ou não existir
        padrao_url = re.compile('(http(s)?://)?(www.)?(bytebank.com(.br)?)(/cambio)')
        # buscar um padrao dentro de uma string
        #busca = padrao_url.search(self.url) # retorna Match
        # verifica se url bate exatamente com o padrao
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é valida"')

    def get_url_base(self):
        # url.find('?') acha a posição do caracter '?'
        indice_interrogacao = self.url.find('?')
        # pega da posição 0 até a posição do caracter "?"
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        # url.find('?') acha a posição do caracter '?'
        indice_interrogacao = self.url.find('?')
        # pega da posição do caracter "?" + 1 e vai até o final
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_url_parametros_valor(self, parametro_busca):
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = url_parametros[indice_valor:]
        else:
            valor = url_parametros[indice_valor:indice_e_comercial]
        return valor

    # retorna um dicionário com os parametros e os valores
    def get_url_parametros_chave_valor(self):
        parametros = self.get_url_parametros().split('&')
        dict_parametros = {}
        for i in range(len(parametros)):
            pos_igual = parametros[i].find('=')
            dict_parametros[parametros[i][:pos_igual]] = parametros[i][pos_igual+1:]
        return dict_parametros

    # retorna o tamanho da url
    def __len__(self):
        return len(self.url)

    # metodo usado para imprimir a class, quando chamar print(nome_da_classe)
    def __str__(self):
        return f'\nURL: {self.url}\nURL Base: {self.get_url_base()}\nParametros: {self.get_url_parametros()}'

    # sobrescreve o metodo __eq__ para comprar se URLs são iguais
    def __eq__(self, other):
        return self.url == other.url


url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
#url = 'https://bytebank.com/cambio?moedaOrigem=real'

extrator_url = ExtratorURL(url)
print(extrator_url.get_url_parametros_chave_valor())


# extrator_url2 = ExtratorURL(url)
# print(extrator_url)
# print(extrator_url == extrator_url2)    # extrator_url.__eq__(extrator_url2)

# print(f'url_base: {extrator_url.get_url_base()}')
# print(f'url_parametros: {extrator_url.get_url_parametros()}')
# print(f'url_parametros_valor: {extrator_url.get_url_parametros_valor("moedaOrigem")}')
# print(f'url_parametros_valor: {extrator_url.get_url_parametros_valor("moedaDestino")}')
# print(f'url_parametros_valor: {extrator_url.get_url_parametros_valor("quantidade")}')
