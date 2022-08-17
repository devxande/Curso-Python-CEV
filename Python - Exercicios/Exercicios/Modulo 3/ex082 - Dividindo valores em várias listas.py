# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = [], pares = [], impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    # SAIR
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar novo valor? [S/N]')).upper().strip()[0]
    if sair == 'N':
        for num in valores:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        valores.sort(), pares.sort(), impares.sort()
        print(f'''*******************
Valores da lista: {valores}
Valores PAR: {pares}
Valores IMPAR: {impares}
** Programa Encerrado **''')
        break
