class Funcionario:
    def __init__(self, nome=''):
        self.nome = nome

    def registara_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


# classe Caelum herda de Funcionario
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

# classe Alura herda de Funcionario
class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no Forum')

# classe criada para retornar o conteudo da classe da classe que herdar essa
# comportamentos que são comuns a todas as classes
# classe Mixin
# exemplo é implentar um classe de log, que pode ser usado em todas as classes
class Hipster:
    def __str__(self) -> str:
        return f'Hispter, {self.nome}'

# classe Junior herda de Alura
class Junior(Alura):
    pass

# classe Pleno herda de Alura e Caelum
class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

jose = Junior()
print('Junior...')
jose.busca_perguntas_sem_resposta()

luan = Pleno()
print('Pleno...')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

joao = Senior('Joao')
print(joao)