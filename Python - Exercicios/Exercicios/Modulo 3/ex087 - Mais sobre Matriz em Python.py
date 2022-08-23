# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = cont2 = pares = impares = terceiraCol = segundaLinha = 0

for cont in range(0, 3):
    for cont2 in range(0, 3):
        matriz[cont][cont2] = int(input(f'Digite um valor para [{cont}, {cont2}]: '))
        # Par e impar
        if matriz[cont][cont2] % 2 == 0:
            pares += matriz[cont][cont2]
        else:
            impares += matriz[cont][cont2]

        # Terceira Coluna
        if cont2 == 2:
            terceiraCol += matriz[cont][cont2]
        cont2 += 1
cont += 1

print(f'{20 * "=-"}')
for cont in range(0, 3):
    for cont2 in range(0, 3):
        print(f'[{matriz[cont][cont2]:^5}]', end='')
    print()
print(f'A soma dos valores PARES: {pares}')
print(f'A soma dos valores IMPARES: {impares}')
print(f'A soma dos valores da terceira Col.: {terceiraCol}')
# Segunda linha
for l in range(0, 3):
    if l == 0:
        segundaLinha = matriz[1][l]
    if matriz[1][l] > segundaLinha:
        segundaLinha = matriz[1][l]
print(f'O MAIOR valor da segunda linha: {segundaLinha}')
