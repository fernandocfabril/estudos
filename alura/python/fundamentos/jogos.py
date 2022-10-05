import forca
import adivinhacao

print('********************************')
print('*******Escolha o seu Jogo!******')
print('********************************')

print("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha o seu jogo: "))

if (jogo == 1):
  print("Jogo da Forca")
  forca.jogar()
elif (jogo == 2):
  print("Jogo de Adivinhação")
  adivinhacao.jogar()

