# criar um ambiente virtual
python -m venv venv

# ativar o ambiente virtual
source venv/Scripts/activate

# instalar a biblioteca pytest
pip install pytest==7.1.2

# criando um arquivo com todas as bibliotecas instaladas
pip freeze >requirements.txt

# criar uma pasta onde ficarão os Testes
## essa pasta tem que ter o nome de 'tests'
## nessa pasta criar um arquivo chamado __init__.py (modulo)

# o da função deve começar sempre com test_
## o o restante precisa ser bem verboso, ou seja, representar bem o que está sendo testado e o resultado esperado, ex:
### def test_quanto_idade_recebe_13_03_2000_deve_retornar_22(self)
### testar uma data 13/03/2000 e esperar receber de retorno 22

# o nome do arquivo 
deve começar o 'test_...
esse arquivo deve estar dentro da pasta tests

# executando o teste
pytest -v
pytest

# executa o teste que tem no nome da função 'idade'
pytest.exe -v -k idade

# executa o teste que tem uma marca chamada 'calcular_bonus'
## @mark.calcular_bonus coloca esse decorator na função que quer testar com essa marca
pytest.exe -v -m calcular_bonus

# criar um arquivo chamado 'pytest.ini' na raiz do projeto
esse arquivo vai servir para informar os Marks que vamos 
utilizar na class TestClass para executarmos um 
teste especifico.
nesse exemplo foi criado o '@mark.calcular_bonus'
para testarmos comente a class 'calcular_bonus'
Para saber mais sobre [pytest](https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark)

# instalar pacote para ver a cobertura de testes
pip install pytest-cov==3.0.0

# ver a cobertura de testes
pytest --cov

# indicar a pasta que vai verificar a cobertura de testes
## `source` é onde está o codigo a ser testado
## `tests` é onde está o codigo de teste
pytest --cov=source tests

# termos faltantes para cobertura de testes
pytest --cov=source tests --cov-report term-missing

# criar um arquivo html com o resultado da cobertura de teste
## cria a pasta htmlcov
pytest --cov=source tests --cov-report html

# para excluir as linhas que não precisam ser testadas
* criar o arquivo `.coveragerc` na raiz do projeto
* adicionar [run] e [report]
* em [report] adicionar as linhas que serão excluidas
    - exclude_lines = 
        def __str__
    será excluida a linha que começa com `def __str__`

# criar um relatório dos testes em forma xml
pytest --junitxml report.xml
pytest --cov-report xml


# O que aprendemos
* O que são teste?
* Criar o primeiro teste automatizado
* Criar testes com o Pytest
* O que é TDD
* Como utilizar o TDD na pratica
* O que são Exceptions?
* Criar testes com Exceptions
* Utilizar markers
* O que é coverage?
* Utilizar o pytest-cov
* Gerar relatórios

# O que fazer agora?
* Personalize o projeto
* Compartilhe nas redes sociais

https://www.alura.com.br/artigos/montando-cenarios-de-testes-com-o-pytest