# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
from time import sleep

ano = int(input('Digite um ano (Para o ano atual digite 0): '))

print('-=-' * 20)
print('Processando...')
print('-=-' * 20)
sleep(3)

# FORMA 1
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))
