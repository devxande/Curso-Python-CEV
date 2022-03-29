# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

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
condicao = 0
print('FORMA 1:')
maior = reta1

# Reta1 Maior
if maior == reta1:
    if reta1 <= reta2 + reta3:
        print('É um {}triangulo!{}'.format(cores['azul'], cores['limpa']))
        condicao = 1
    else:
        print('Não é um triangulo!')

# Reta2 Maior
if reta2 > reta1 and reta2 > reta3:
    maior = reta2
    if reta2 <= reta1 + reta3:
        print('É um triangulo!'.format(cores['azul'], cores['limpa']))
        condicao = 1
    else:
        print('Não é um triangulo!')

# Reta3 Maior
if reta3 > reta1 and reta3 > reta2:
    maior = reta3
    if reta3 <= reta1 + reta2:
        print('É um triangulo!'.format(cores['azul'], cores['limpa']))
        condicao = 1
    else:
        print('Não é um triangulo!')

# Tipo do Triângulo
if condicao == 1:
    if reta1 == reta2 == reta3:
        print('O triângulo é Equilátero')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é Escaleno')
