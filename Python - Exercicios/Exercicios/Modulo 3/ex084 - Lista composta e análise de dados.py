# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
maiorPeso = menorPeso = 0

while True:
    dados.append(str(input('Digite o NOME: ')))
    dados.append(int(input('Digite o PESO: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        elif dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    # SAIR
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar nova pessoa? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break

print(f'''\n{20 * "*"}
Número de pessoas cadastradas: {len(pessoas)}''')
print(f'MAIOR Peso foi de {maiorPeso} - Pessoas:', end=' ')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'{p[0]}', end=' ')
print(f'\nMENOR Peso foi de {menorPeso} - Pessoas:', end=' ')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'{p[0]}', end='')
