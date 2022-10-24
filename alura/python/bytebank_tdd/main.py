from bytebank import Funcionario 

# fernando = Funcionario('Fernando Fabril', '20/11/1973', 5000)
# print(fernando)
# print(fernando.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '20/11/1973', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

#teste_idade()

def teste_decrescimo_salario():
    entrada_salario = 100000.00    # Given-Contexto
    entrada_nome = 'Paulo Bragança'
    esperado = 90000.00
    print(type(entrada_salario), type(esperado))
    funcionario_teste = Funcionario('Fernando', '11/11/2000', 10000)
    print(funcionario_teste._salario)
    print(funcionario_teste.salario)
    #funcionario_teste.decrescimo_salario() # When
    #resultado = funcionario_teste.salario()
    
    #print(resultado, esperado)

teste_decrescimo_salario()