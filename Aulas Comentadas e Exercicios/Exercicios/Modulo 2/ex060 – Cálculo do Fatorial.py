# Exercício Python 060: Faça um programa que leia um número qualquer
# e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
num = int(input('\033[1;35m*Calculadora Fatorial*\033[m\nDigite um valor: '))
cont=num
teste=num
print(f'Calculando {num}! = ', end='')
while cont != 1:
    num = num * (cont - 1)
    print(f'{cont}x',end='')
    cont-=1
print(f'1= {num}')

#Import do Factorial
print('Teste com Import: {}'.format(factorial(teste)))