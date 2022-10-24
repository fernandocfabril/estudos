from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario


    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return float(self._salario)

    def idade(self):
        ano_atual = date.today().year
        # separa as informações da data em lista e pega o ultimo item da lista
        # usa "/" para separar as informaçoes da data
        ano_nascimento = self._data_nascimento.split('/')[-1]
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        # remove os epaços em brando de antes e dpois da string
        nome_completo = self.nome.strip()
        # separa os nomes por ' ' e retorna uma lista, onde cada elemento é o nome do funcionario
        nome_separado = nome_completo.split(' ')
        # retorna o ultimo item da lista
        return nome_separado[-1]

    def _eh_socio(self):
        # sobrenome dos diretores que não podem ganhar mais que 100000
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._eh_socio():
            # tira 10% do salario
            decrescimo = self._salario * 0.10
            self._salario -= decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            #valor = 0
            raise Exception('O salário é muito alto para receber um bônus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'