# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep

num = int(input('Digite um valor inteiro: '))

# O operador % pega o resto de um numero.
result = num % 2

print('Processando...')
sleep(2)

print('Seu número é impar!' if result == 1 else 'Seu numero é par!')
