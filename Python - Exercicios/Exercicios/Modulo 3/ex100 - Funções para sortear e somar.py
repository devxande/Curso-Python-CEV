# criar funçao sorteia() e somaPar()
# Vai sortear 5 numeros e colocar na lista
# mostrar todos valores pares sorteados.

from random import choice
from time import sleep


def sorteia(lst):
    numeros = []
    for cont in range(0, 5):
        while True:
            valor = choice(lst)
            if valor not in numeros:
                numeros.append(valor)
                break
    print(f'Sorteando 5 valores da lista: ', end='')
    for v in numeros:
        sleep(0.3)
        print(v, end=' ')
    print('PRONTO!')
    return numeros


def somaPar(lst):
    par = 0
    for v in lst:
        if v % 2 == 0:
            par += v
    sleep(0.3)
    print(f'Somnando os valores pares de {lst}, temos {par}.')


# PROGRAMA PRINCIPAL
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somaPar(sorteia(lista))
