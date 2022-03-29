# Exercício Python 038: Escreva um programa que leia dois números inteiros
# e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('***PROGRAMA INICIADO***\nDigite o primeiro numero: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é o maior: {num1}')
elif num2 > num1:
    print(f'O segundo número é o maior: {num2}')
else:
    print('Os numeros digitados são iguais.')
