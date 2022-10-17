from collections import Counter

def analisa_frequencia_de_letras2(texto):
    # cria uma dicionário com as letras e o numero de vezes que ela aparece
    aparicoes = Counter(texto.lower())
    print(aparicoes)

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  print("{} => {:.2f}%".format(caractere, proporcao * 100))


def analisa_frequencia_de_palavras(texto):
    # cria uma dicionário com as letras e o numero de vezes que ela aparece
    aparicoes = Counter(texto.lower().split())
    #print(aparicoes)
    print(aparicoes.most_common(10))
    total_palavras = sum(aparicoes.values())
    for palavra, proporcao in aparicoes.most_common(10):
        print(f'{palavra}, {(proporcao/ total_palavras * 100):.2f}%')
    

texto1 = '''
Uma dúvida muito comum entre as pessoas que começam a se interessar e estudar assuntos na área de dados é como organizar os aprendizados, o que elas devem aprender primeiro e quais áreas de conhecimentos elas precisam se engajar mais.

Isso é completamente natural, já que a área de dados possui uma gama extensa de subcategorias e vertentes. Para conseguir determinar por qual caminho seguir, precisamos entender esses percursos e quais aprendizados cada um deles nos oferece.

Neste artigo, mostraremos os possíveis caminhos e trilhas de estudos disponíveis dentro da aba Escola de Data Science no site da Alura, desde o básico até o avançado, para te ajudar a criar um plano de estudos eficiente e direcionado ao seu objetivo, vamos lá?

Aqui na nossa plataforma já dividimos os conteúdos em subcategorias, mas sabemos que para as pessoas que acabaram de ter seu primeiro contato com a área, isso pode não ser o suficiente.
Ter uma base de conhecimentos em SQL e Banco de Dados é um ótimo começo, independente de quais forem seus próximos passos é interessante entender sobre esses temas.

Temos três planos de estudos bem completos para essa subcategoria, cada um com conteúdos do básico ao avançado, a diferença entre eles será o SGBD (Sistema Gerenciador de Banco de Dados) que será utilizado durante os cursos.

Você pode escolher começar pela formação com o SGBD que mais tem interesse em aprender primeiro:
'''

name_file = 'texto_ingles.txt'
with open(name_file, 'r', encoding='utf-8') as file:
    texto = file.read()
#print(texto.lower().split())
#analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_palavras(texto)
