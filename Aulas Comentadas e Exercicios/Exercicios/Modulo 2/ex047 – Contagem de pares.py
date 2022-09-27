# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1, 50 + 1):
    # % pega o resto da divisão 0=par 1=impar
    par = c % 2
    if par == 0:
        print(f'O numero {c} é PAR!')
