from abc import ABCMeta, abstractmethod

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

    def __str__(self):
        return f'Codigo {self._codigo} Saldo {self._saldo}'


conta1 = ContaSalario(37)
print(conta1)
conta2 = ContaSalario(37)
print(conta2)
conta3 = ContaSalario(38)
print(conta3)

# é necessário implementar o metodo __eq__ na classe ContaSalario
print(conta1 == conta2, id(conta1), id(conta2))
print(conta1 == conta3, id(conta1), id(conta3))

# verifica se a instancia é do tipo da classe
#isinstance(ContaCorrente(34), ContaCorrente)
print(isinstance(ContaSalario(34), ContaSalario))