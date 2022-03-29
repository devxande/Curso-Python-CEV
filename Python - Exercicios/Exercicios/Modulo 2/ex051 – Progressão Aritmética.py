# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pa=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))

for c in range(1,11):
    pa += razao
    print(f'O termo {c} tem a PA:{pa}')
