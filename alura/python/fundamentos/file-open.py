arquivo = open('pessoas.txt', 'r', encoding='utf-8')
# le o arquivo inteiro
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


with open('pessoas.txt', 'r', encoding='utf-8') as file:
    # le uma linha
    ##print(file.readline())
    for linha in file:
        print(linha.strip())

palavras = []
with open('palavras_forca.txt', 'r') as file:
    palavras = [ linha.strip().upper() for linha in file ]

print(palavras)


