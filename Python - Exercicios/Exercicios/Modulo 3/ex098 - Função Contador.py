# criar funçao contador()
# Recebe 3 parametros, inicio, fim e passo.
# mostrar 3 contagens: 1 até 10, de 1 em 1
# 10 até 0, de 2 em 2
# contem personalizada: inicio maior ele volta; valor do passo negativo, vira 1; se passo zero vira 1 em 1.

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
    if passo < 0 or passo == 0:
        passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for cont in range(inicio, fim - 1, passo * (-1)):
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
print()
lin()
contador(10, 0, 2)
contadorPersonalizado()
