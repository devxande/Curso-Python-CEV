# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite ultimo numero: '))

# FORMA 1
print('FORMA 1:')
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O maior valor é {}! \nO menor valor é {}!'.format(maior, menor))

# FORMA 2
print('FORMA 2:')
if num1 > num2:
    if num1 > num3:
        print('{} é o maior.'.format(num1))
    else:
        print('{} é o maior.'.format(num3))
else:
    if num2 > num3:
        print('{} é o maior.'.format(num2))
    else:
        print('{} é o maior.'.format(num3))

if num1 < num2:
    if num1 < num3:
        print('{} é o menor.'.format(num1))
    else:
        print('{} é o menor.'.format(num3))
else:
    if num2 < num3:
        print('{} é o menor.'.format(num2))
    else:
        print('{} é o menor.'.format(num3))
