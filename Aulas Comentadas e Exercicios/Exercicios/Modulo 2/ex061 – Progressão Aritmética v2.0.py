# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

pa=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=1
while cont < 11:

    print(f'O termo {cont} tem a PA:{pa}')
    pa += razao
    cont+=1
#for c in range(1,11):
#   pa += razao
#   print(f'O termo {c} tem a PA:{pa}')
