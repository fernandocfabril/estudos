from unittest import result
from source.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    # as funções de testes devem sempre começar om 'test_'
    def test_quanto_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()   #When-ação

        assert resultado == esperado    # Then-desfecho

    def test_quando_sobrenome_recebe_Fernando_Carlos_Fabril_deve_retornar_Fabril(self):
        entrada = '   Fernando Carlos Fabril   '    #Given-Contexto
        esperado = 'Fabril'

        fernando = Funcionario(entrada, '11/11/2000', 1111)
        resultado = fernando.sobrenome()    #When-Ação

        assert resultado == esperado    #Then=Desfecho

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(sef):
        entrada_salario = 100000    # Given-Contexto
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado    # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  #Given
        esperado = 100

        funcionario_teste = Funcionario('Fernando', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado    # Then

    # informa um marca para ser usado na hora de chamar o pytest
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000000_deve_retornar_exception(self):
        # trata o retorno com Exception
        with pytest.raises(Exception):
            entrada = 1000000000    # Given

            funcionario_teste = Funcionario('Fernando', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado    # Then

    # esse teste não faz sentido, porque é uma implementação da propria linguagem e não um lógica/regra de negocio
    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000    # Given
    #     esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__() # When

    #     assert resultado == esperado    # Then