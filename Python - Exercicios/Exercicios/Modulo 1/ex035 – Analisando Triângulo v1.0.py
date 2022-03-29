# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep

cores = {
    'azul': '\033[34m',
    'vermelho': '\033[31m',
    'amarelho': '\033[33m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'limpa': '\033[m'
}

reta1 = float(input('Digite 1º segmento: '))
reta2 = float(input('Digite 2º segmento: '))
reta3 = float(input('Digite 3º segmento: '))

print('-=-' * 10, '\nProcessando...\n', '-=-' * 10)
sleep(0)

print('FORMA 1:')
maior = reta1
if reta2 > reta1 and reta2 > reta3:
    maior = reta2
    print('É um triangulo!' if reta2 < reta1 + reta3 else 'Não é um triangulo!')
if reta3 > reta1 and reta3 > reta2:
    maior = reta3
    print('É um triangulo!' if reta3 < reta1 + reta2 else 'Não é um triangulo!')
if maior == reta1:
    print(
        'É um {}triangulo!{}'.format(cores['azul'], cores['limpa']) if reta1 < reta2 + reta3 else 'Não é um triangulo!')
