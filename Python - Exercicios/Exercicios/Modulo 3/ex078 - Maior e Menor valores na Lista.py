# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

posicaoMaior = posicaoMenor = pos = 0
valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f"Você digitou os valores: {valores}.")
print(f"O maior valor é: {max(valores)}, ", end='')
print(f'nas posições:', end='')
for pos, posicaoMaior in enumerate(valores):
    if posicaoMaior == max(valores):
        print(f' {pos}...', end='')

pos = 0
print(f"\nO menor valor é: {min(valores)}, ", end='')
print(f'nas posições:', end='')
for pos, posicaoMenor in enumerate(valores):
    if posicaoMenor == min(valores):
        print(f' {pos}...', end='')