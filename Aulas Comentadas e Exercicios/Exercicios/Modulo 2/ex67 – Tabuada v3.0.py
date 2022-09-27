# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    cont = 1
    num = int(input(f'{10 * "-"}\nDigite um valor para tabuada:\n{10 * "-"}> '))
    if num < 0:
        break
    while cont < 11:
    #for cont range(1,11):
        print(f'{cont} x {num} = {cont * num}')
        cont += 1
print('Programa finalizado.')
