# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

preco = total = primeiro = barato = milReais = 0
nomeBarato=''

while True:
    nome = str(input(f'{20*"="}\nDigite um nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))

    # Total
    total += preco
    # +1000 reais
    if preco > 1000:
        milReais += 1
    # Nome +Barato
    if primeiro == 0:
        barato = preco
        nomeBarato = nome
        primeiro = 1
    else:
        if preco<barato:
            barato = preco
            nomeBarato=nome
    # Sair
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Gostaria de adicionar novo produto?')).upper().strip()[0]
    if sair == 'N':
        break
print(f'{20*"="}O valor total da compra é: R${total:.2f}\nO produto mais barato: {nomeBarato}\nTem {milReais} produto(s) mais de 1000 reais; ')