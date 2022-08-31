# Exercício Python 100: Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


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
    print(f'Somando os valores pares de {lst}, temos {par}.')


# PROGRAMA PRINCIPAL
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somaPar(sorteia(lista))
