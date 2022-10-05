import random


# gera um numero aleatorio entre 0.0 e 1.0
numero_random = random.random()
print(f'numero entre 0.0 e 1.0 {numero_random}')
print(f'numero entre 1.0 e 10.0 {numero_random * 10}')
print(f'numero entre 1.0 e 100.0 {numero_random * 100}', end='\n\n')

print(f'numero inteiro entre 0 e 1 {int(numero_random)}')
print(f'numero inteiro entre 1 e 10 {int(numero_random * 10)}')
print(f'numero inteiro entre 1 e 100 {int(numero_random * 100)}', end='\n\n')

print(f'numero inteiro arredondando entre 0 e 1 {round(numero_random)}')
print(f'numero inteiro arredondando entre 1 e 10 {round(numero_random * 10)}')
print(f'numero inteiro arredondando entre 1 e 100 {round(numero_random * 100)}', end='\n\n')