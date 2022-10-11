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

    # representação em texto do objeto, é o que vai aparecer na tela quando executar o comando print(Filme)
    def __str__(self):
        return f'Nome: {self._nome} - Likes: {self._likes}'


# classe filha que extends a classe mãe (Programa)
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # inicializa o objeto com os atributos da classe superclass/mãe
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'Nome: {self._nome} - Ano: {self.ano} '
    #   f'- Duracao {self.duracao} - Likes {self._likes}')

    # essa função determina o que a classe vai imprimir, ou seja, imprime o conteúdo da classe como texto e substitui o metodo imprime(self)
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duracao {self.duracao} - Likes {self._likes}'

# classe filha que extends a classe mãe (Programa)
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # inicializa o objeto com os atributos da classe superclass/mãe
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f'Nome: {self._nome} - Ano: {self.ano} '
    #   f'- Temporadas {self.temporadas} - Likes {self._likes}')

    # essa função determina o que a classe vai imprimir, ou seja, imprime o conteúdo da classe como texto e substitui o metodo imprime(self)
    def __str__(self) -> str:
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas {self.temporadas} - Likes {self._likes}'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#       f'- Duração: {vingadores.duracao} - Likes {vingadores.likes}')

# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#       f'- Temporadas: {atlanta.temporadas} - {atlanta.likes} \n')

# cria uma lista com os objetos
filmes_e_series = [vingadores, atlanta]

# itera sobre alista e imprime os atributos dos objetos
# for programa in filmes_e_series:
#     # operador ternario
#     detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
#     # if hasattr(programa, 'duracao'):
#     #     detalhes = programa.duracao
#     # else:
#     #     detalhes = programa.temporadas
#     print(f'Programas -> Nome: {programa.nome} - Ano: {programa.ano} '
#           f'- Temporadas: {detalhes} - {programa.likes}')

for programa in filmes_e_series:
    # polimorfismo, não importa qual é a classe que tem o metodo imprimte()
    # programa.imprime()
    print(programa)
