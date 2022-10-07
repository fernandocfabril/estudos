import random

def carregar_palavra_secreta():
    palavras = []
    # le o arquivo
    with open('palavras_forca.txt', 'r') as file:
        # adicona as linhas em um lista, elimina os caracteres especiais e os espaços em branco e 
        # transforma as palavras em maiscula
        palavras = [ linha.strip().upper() for linha in file ]

    numero = random.randint(0, len(palavras) - 1)
    return palavras[numero]


def jogar():
    print('********************************')
    print('**Bem vindo no jogo da Forca!***')
    print('********************************')

    palavra_secreta = carregar_palavra_secreta()

    # List Comprehension
    letras_acertadas = ['_' for letra in palavra_secreta] # ou ['_'] * len(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    num_tentativas = 7

    print(letras_acertadas)
    while (not enforcou and not acertou):
        
        print(f'Faltam {letras_acertadas.count("_")} letras')
        print(f'Faltam {num_tentativas - erros} tentativas')

        chute = input("Digite uma letra: ")

        # remove os espaços em brando no inicio e final
        chute = chute.strip()

        # transforma em maiscula
        chute = chute.upper()
        
        # mostra o indice da letra na palavra
        # se a letra tiver mais de uma vez na palavra, retorna
        # o indice a primeira ocorrencia
        if chute in palavra_secreta:
            print(f"{palavra_secreta.find(chute)}")

            for i, letra in enumerate(palavra_secreta):
                
                # transforma a letra em maiscula
                if letra == chute:
                    letras_acertadas[i] = chute
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)

        # eforca quando o numero de erros for igual ao tamanho da palavra secreta
        enforcou = (erros == num_tentativas)
        # acertou quando o caracter "_" não tiver mais em letras_acertadas
        acertou = ("_" not in letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo!")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# essa condição é pra quando o programa for chamado pela linha de comando
# quando for feito o import desse programa em outro, esse if não será executado
if (__name__ == "__main__"):
  jogar()