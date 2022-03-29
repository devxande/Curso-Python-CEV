# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

from math import floor,trunc
real=float(input('Digite um número real:'))
print('o numero {:.2f} tem a parte inteira {}'.format(real,floor(real)))
print('o numero {:.2f} tem a parte inteira {}'.format(real,int(real)))
print('o numero {:.2f} tem a parte inteira {}'.format(real,trunc(real)))
