import random

def jogar():
    print('********************************')
    print('Bem vindo no jogo de Advinhação!')
    print('********************************')

    # random.random() -> gera um numero entre 0.0 e 1.0
    #numero_secreto = round(random.random() * 100)
    # gera um numero inteiro entre 1 e 100
    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print("Qual nível de dificuldade ? ")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Define o nível de dificuldade: "))

    if (nivel == 1 ):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        #print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            # volta para o inicio do FOR
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print(f"Você digitou {chute}")

        if acertou:
            print("Você acertou e fez {pontos} pontos!")
            # sai do FOR
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            if maior:
                print("Você digitou um valor maior")
                if (rodada == total_de_tentativas):
                    print(f"O numero secreto é {numero_secreto}. Você fez {pontos} pontos.")
            else:
                print("Você digitou um valor menor")
                if (rodada == total_de_tentativas):
                    print(f"O numero secreto é {numero_secreto}. Você fez {pontos} pontos.")

    print("Fim do jogo!")


# essa condição é pra quando o programa for chamado pela linha de comando
# quando for feito o import desse programa em outro, esse if não será executado
if (__name__ == "__main__"):
    jogar()