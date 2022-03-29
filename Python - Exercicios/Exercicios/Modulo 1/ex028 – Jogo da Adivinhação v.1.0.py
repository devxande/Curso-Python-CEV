# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
from time import sleep

# Pode importar o randint, que ficaria
# sorteio = randint(1,5)

print('-=-' * 20)
sorteio = choice([1, 2, 3, 4, 5])
adivinha = int(input('Digite um valor de 1 a 5: '))
print('-=-' * 20)

print('Processando...')
sleep(0)

# Simplificada
print('Você acertou!' if adivinha == sorteio else 'Voce errou.')

# Composta
if adivinha == sorteio:
    print('Voce acertou.')
else:
    print('Voce errou.')

print('O numero correto era {}'.format(sorteio))
