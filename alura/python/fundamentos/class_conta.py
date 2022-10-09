
class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f'Contruindo objeto... {self}')
        # quando o atributo começa com __ ele é fica privado e não permite o acesso direto, somente através dos metodos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    # metodo privado criado para verificar se pode sacar o valor informado no metodo saca(self, valor)
    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print('Saque efetuado!!!')
        else:
            return f'O valor {valor} passou do limite disponivel'

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    # o @property subistitui a criação de um metodo chamado get_titular(self)
    # assim o nome do metodo fica igual ao atributo
    @property
    def titular(self):
        return self.__titular

    # o @property subistitui a criação de um metodo chamado get_saldo(self)
    # assim o nome do metodo fica igual ao atributo
    @property
    def saldo(self):
        return self.__saldo

    # o @property subistitui a criação de um metodo chamado get_limite(self)
    # assim o nome do metodo fica igual ao atributo
    @property
    def limite(self):
        return self.__limite
    
    # o @limite.setter subistitui a criação de um metodo chamado set_limite(self, limite)
    # assim o nome do metodo fica igual ao atributo
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # metodo estatico, esse metodo funciona sem a necessidade de instanciar a classe, são chamados metodos da Classe
    @staticmethod
    def codigo_banco():
        return '001'

    # metodo estatico, esse metodo funciona sem a necessidade de instanciar a classe, são chamados metodos da Classe
    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

if (__name__ == '__main__'):
    conta1 = Conta(1, 'Antonio', 12.0)
    conta2 = Conta(2, 'João', 50.0)
    conta3 = Conta(3, 'José', 100.0, 3000.0)

    # print(f'Limite do {conta1.titular} {conta1.limite}')
    # print(f'Limite do {conta2.titular} {conta2.limite}')
    # print(f'Limite do {conta3.titular} {conta3.limite}')

    # conta1.extrato()
    # conta1.deposita(55.6)
    # conta1.extrato()
    # conta1.saca(0.6)
    # conta1.extrato()
    conta1.extrato()
    conta3.extrato()
    conta3.transfere(10, conta1)
    conta1.extrato()
    conta3.extrato()
    print(f'Titular {conta1.titular}, saldo {conta1.saldo} e limite {conta1.limite}')
    conta1.saldo
    conta1.limite = 2000
    print(f'Titular {conta1.titular}, saldo {conta1.saldo} e limite {conta1.limite}')

    # lima a referenica do objeto, conta1 não é mais um objeto da Classe Conta
    conta1 = None


