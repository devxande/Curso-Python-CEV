# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = cont2 = 0

for cont in range(0, 3):
    for cont2 in range(0, 3):
        matriz[cont][cont2] = int(input(f'Digite um valor para [{cont}, {cont2}]: '))
        cont2 += 1
cont += 1
print(f'{20 * "=-"}')
for cont in range(0, 3):
    for cont2 in range(0, 3):
        print(f'[{matriz[cont][cont2]:^5}]', end='')
    print()
