# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

sorteio = []
lista = []
numero = cont = 0

jogos = int(input(f'''{10 * "-=-"}
{"MEGA SENA DO XANDAO":<10}
{10 * "-=-"}
Digite quantos jogos voce quer: '''))
for cont in range(0, jogos):
    for cont2 in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                break
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
sleep(0.5)
for cont in range(0, jogos):
    print(f'JOGO {cont + 1}: {sorteio[cont]}')
    sleep(1)
print('-=' * 5, 'BOA SORTE', '=-' * 5)
