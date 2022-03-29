# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

sorteio = randint(1, 10)
adivinha = 0
cont = 0
print('-=-' * 10)
while adivinha != sorteio:
    adivinha = int(input('Digite um valor de 1 a 10: '))
    if adivinha<sorteio:
        print('Quase, o número é maior...\n')
    elif adivinha>sorteio:
        print('Quase! o número é menor...\n')
    cont += 1

print('-=-' * 10)
print('Processando...')
sleep(0)

# Simplificada
print(f'Você acertou! Após {cont} tentativas.')
# Composta
# if adivinha == sorteio:
#    print('Voce acertou.')
# else:
#    print('Voce errou.')

print('O numero correto: \033[35m{}'.format(sorteio))
