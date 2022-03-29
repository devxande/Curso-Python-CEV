# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule
# e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média das notas {} e {} é: {}'.format(n1, n2, media))
