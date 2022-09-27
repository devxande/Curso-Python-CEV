# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def lin():
    print(f'-=-' * 20)


def contadorPersonalizado():
    lin()
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    lin()
    contador(inicio, fim, passo)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo * (-1)} em {passo * (-1)}')
        for cont in range(inicio, fim - 1, passo):
            sleep(0.3)
            print(f'{cont}', end=' ')
        print('FIM!')
    else:
        if inicio <= fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            for cont in range(inicio, fim + 1, passo):
                sleep(0.3)
                print(f'{cont}', end=' ')
            print('FIM!')
        else:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            for cont in range(inicio, fim - 1, passo * (-1)):
                sleep(0.3)
                print(f'{cont}', end=' ')
            print('FIM!')


# PROGRAMA PRINCIPAL
lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
contadorPersonalizado()
