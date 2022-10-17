from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering

# fazer a ordenação total: eq, lt, le, gt, ge
# pra isso é necessário implementar pelo menos __eq__ e __lt__
@total_ordering
class Conta(metaclass=ABCMeta):
  
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    # o metodo abstrato obriga as classes filhas a definerem um metodo com o mesmo nome
    # se não definir, vai dar erro quando for instaciar
    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaPoupanca(Conta):
  
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

class ContaCorrente(Conta):
  
    def deposita(self, valor):
        self.saldo += valor

    def passa_o_mes(self):
        self._saldo -= 2

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposito(self, valor):
        self._saldo += valor

    def __eq__(self, other):
        # verifica se os tipos dos objetos são iguais
        if type(other) != ContaSalario:
            return False
        else:
            return self._codigo == other._codigo

    # função para fazer a ordenação da class
    def __lt__(self, other):
        # se o saldo for igual, retorna a conta com menor numero
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._saldo < other._saldo

    def __str__(self):
        return f'Codigo {self._codigo} Saldo {self._saldo}'


conta1 = ContaSalario(37)
conta1.deposito(200)
print(conta1)
conta2 = ContaSalario(37)
conta2.deposito(120)
print(conta2)
conta3 = ContaSalario(38)
conta3.deposito(100)
print(conta3)

# é necessário implementar o metodo __eq__ na classe ContaSalario
print(conta1 == conta2, id(conta1), id(conta2))
print(conta1 == conta3, id(conta1), id(conta3))

# verifica se a instancia é do tipo da classe
#isinstance(ContaCorrente(34), ContaCorrente)
print(isinstance(ContaSalario(34), ContaSalario))

contas = [conta1, conta2, conta3]
for conta in contas:
    print(conta)

# ordenar a lista de classes conta
print('ordenação de classes')
def extrai_saldo(conta):
    return conta._saldo
for conta in sorted(contas, key=extrai_saldo):
    print(conta)

print('outra maneira de ordenação de classes')
for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

print('ordenação de classes')
for conta in sorted(contas):
    print(conta)
print('ordenação invertida de classes')
for conta in sorted(contas, reverse=True):
    print(conta)
