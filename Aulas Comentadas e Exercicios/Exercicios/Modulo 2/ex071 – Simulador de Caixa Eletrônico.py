# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cinquenta = vinte = dez = um = 0

# Título e Input
valor = int(input(f'''{20 * "="}
\033[35mBANCO DO XANDON\033[m
{20 * "="}
Digite o valor a ser sacado: '''))

# Cédulas de R$50,00
if valor >= 50:
    cinquenta = int(valor / 50)
    valor = valor - (cinquenta * 50)
    print(f'São {cinquenta} cédulas de R$50,00.')

# Cédulas de R$20,00
if valor >= 20:
    vinte = int(valor / 20)
    valor = valor - (vinte * 20)
    print(f'São {vinte} cédulas de R$20,00.')

# Cédulas de R$10,00
if valor >= 10:
    dez = int(valor / 10)
    print(f'São {dez} cédulas de R$10,00.')
    valor = valor - (dez * 10)

# Cédulas de R$1,00
if valor != 0:
    um = valor
    print(f'São {um} cédulas de R$1,00.')

print('\n\033[31mPrograma finalizado.')
