class Professor():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # metodo get para pegar a informação
    @property
    def nome(self):
        return self.__nome

    # metodo set para atualizar a informação no atributo
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
