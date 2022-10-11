# classe mãe
# o uso de um underline só no atributo não o torna privado, mas
# por convenção indica ao programador que não é para usar
# atributos privados não vão para a classe filha
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # get_nome()
    @property
    def nome(self):
        return self._nome

    # set_nome()
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # get_nome()
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

# classe filha que extends a classe mãe (Programa)
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # inicializa o objeto com os atributos da classe superclass/mãe
        super().__init__(nome, ano)
        self.duracao = duracao

# classe filha que extends a classe mãe (Programa)
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # inicializa o objeto com os atributos da classe superclass/mãe
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Likes {vingadores.likes}')

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} - {atlanta.likes}')


