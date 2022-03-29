# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um Valor [999 para sair]:  '))
    if num != 999:
        cont += 1
        soma += num
print(f'Foram digitados {cont} números.\nA soma entre eles é {soma}.')
