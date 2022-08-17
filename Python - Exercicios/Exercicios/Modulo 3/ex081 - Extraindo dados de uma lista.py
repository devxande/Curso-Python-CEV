# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))

    # SAIR
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar novo valor? [S/N]')).upper().strip()[0]
    if sair == 'N':
        valores.sort(reverse=True)

        print(f'''\n***** RESULTADO *****
Numeros Digitados: {len(valores)}.
Lista em Ordem Decrescente: {valores}''')
        if 5 in valores:
            print('Lista contem o número 5!')
        else:
            print('Lista NÃO contem o numero 5!')
        print('\n***Programa Encerrado***')
        break
