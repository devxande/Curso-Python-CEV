# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Digite um arrombado:'))
n2 = str(input('Digite um arrombado 2:'))
n3 = str(input('Digite um arrombado 3'))
lista = [n1, n2, n3]
shuffle(lista)
print(lista)
