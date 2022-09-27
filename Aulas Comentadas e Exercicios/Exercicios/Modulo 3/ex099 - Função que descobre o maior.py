# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def lin():
    print(f'-=-' * 20)


def maior(lst):
    lin()
    print('Analisando os valores passados...')
    pos = 0
    while pos < len(lst):
        sleep(0.3)
        print(f'{lst[pos]}', end=' ')
        pos += 1
    print(f'\nForam informados {len(lst)} números ao todo.')
    print(f'O maior valor informado foi o {max(lst)}.')


# PROGRAMA PRINCIPAL
lista = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    # SAIR
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar novo número? [S/N]')).upper()[0]
        if sair not in 'SN':
            print('Opção invalida!')
    if sair == 'N':
        break
maior(lista)
