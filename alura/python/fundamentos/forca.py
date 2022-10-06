
def jogar():
    print('********************************')
    print('**Bem vindo no jogo da Forca!***')
    print('********************************')

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")

        # remove os espaços em brando no inicio e final
        chute = chute.strip()
        # mostra o indice da letra na palavra
        # se a letra tiver mais de uma vez na palavra, retorna
        # o indice a primeira ocorrencia
        print(f"{palavra_secreta.find(chute)}")

        for i, letra in enumerate(palavra_secreta):
            
            # transforma a letra em maiscula
            if letra.strip().upper() == chute.strip().upper():
                print(i, letra)

    print("Fim do jogo!")

# essa condição é pra quando o programa for chamado pela linha de comando
# quando for feito o import desse programa em outro, esse if não será executado
if (__name__ == "__main__"):
  jogar()