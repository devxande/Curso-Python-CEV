# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date

atual = date.today().year
maior = 0
menor = 0
for c in range(1, 7 + 1):
    ano = int(input(f'Digite data de nascimento da {c}ª pessoa: '))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'Do grupo de pessoas {maior} são maiores e {menor} menores de idade.')
