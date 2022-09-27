#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
lista = [n1, n2, n3]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
