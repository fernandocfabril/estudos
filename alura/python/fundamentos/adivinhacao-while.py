print('********************************')
print('Bem vindo no jogo de Advinhação!')
print('********************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print(f"Você digitou {chute}")

    if acertou:
        print("Você acertou")
    elif maior:
        print("Você digitou um valor maior")
    else:
        print("Você digitou um valor menor")

    rodada += 1

    print("Fim do jogo!")
