# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

num = int(input('Digite um valor para a sequencia de Fibonacci: '))
cont = 0
total = 1
antecessor = 0
print(antecessor, end='->')
while cont < num:
    print(total, end='->')
    outro = total
    total = antecessor + total
    antecessor = outro
    cont += 1
print('Fim')