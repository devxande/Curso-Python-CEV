# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'**O maior peso lido é {maior,:.2f}\n**O menor peso lido é {menor,:.2f}')
