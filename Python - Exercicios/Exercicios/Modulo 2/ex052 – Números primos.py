# Exercício Python 52: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num1 = int(input('Digite um número: '))
s = 0
for c in range(1, num1 + 1):
    if num1 % c == 0 and num1 % 1 == 0:
        s += 1
        print(f'\033[33m{c}\033[m', end=(' '))
    else:
        print(f'\033[31m{c}\033[m', end=(' '))


print(f'\nO numero {num1} é primo!' if s == 2 else f'O numero {num1} não é primo!')
