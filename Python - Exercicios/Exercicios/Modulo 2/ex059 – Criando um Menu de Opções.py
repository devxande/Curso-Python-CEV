# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
# Cores.
color = {
    'lateral': '\033[m''\033[7;1;40m''*''\033[m',
    'star': '\033[7;1;40m',
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'blue': '\033[1;34m',
    'purple': '\033[1;35m',
    'purpleFundo': '\033[35;1;40m',
    'blackFundo': '\033[;1;40m',
    'bold': '\033[1m',
    'clear': '\033[m',
}

first = 0
second = 0
choice = 4

while choice != 5:
    # Primeiro ou troca de valores.
    if choice == 4:
        first = int(input(f'{color["purple"]}{5*"_"}NOVOS VALORES{5*"_"}{color["clear"]}\nDigite o primeiro valor: '))
        second = int(input('Digite o segundo valor: '))
        print('Carregando...'), sleep(0.5)

    # Menu.
    choice = int(input(f'''\n{color['purpleFundo']}{20*":) "}{color['clear']}
{color['blackFundo']}Calculadora do Xandon{color['clear']}
{color['green']}[1]{color['clear']} Somar Valores
{color['yellow']}[2]{color['clear']} Multiplicar Valores
{color['blue']}[3]{color['clear']} Maior Valor
{color['purple']}[4]{color['clear']} Novos Valores
{color['red']}[5]{color['clear']} Sair do Programa
{color['blackFundo']}Escolha a opcao:{color['clear']} '''))
    print('Carregando...'), sleep(0.5)

    # [1] Somar Valores
    if choice == 1:
        print(f'''\n{color["green"]}{5*"_"}SOMA VALORES{5*"_"}{color["clear"]}
A soma dos valores {first} e {second} é igual a {first+second}.
Calculo: {first}+{second}={first+second}\n''')

    # [2] Multiplicar Valores
    elif choice == 2:
        print(f'''\n{color["yellow"]}{5*"_"}MULTI. VALORES{5*"_"}{color["clear"]}\n
A multiplicação dos valores {first} e {second} é igual a {first*second}.
Calculo: {first}*{second}={first*second}\n''')

    # [3] Maior Valor
    elif choice == 3:
        print(f'''\n{color["blue"]}{5*"_"}MAIOR VALOR{5*"_"}{color["clear"]}
Entre os valores {first} e {second} o maior é {first if first>second else second}.\n''')

print(f'\n{color["red"]}Programa Finalizando...{color["clear"]} \nBye'), sleep(0.5)