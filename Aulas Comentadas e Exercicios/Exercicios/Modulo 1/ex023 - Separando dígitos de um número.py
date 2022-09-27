# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

import math
numero = int(input('Digite um valor de 0 a 9999:'))

milhar = math.floor(numero/1000)
print('O milhar no seu número é: {}'.format(milhar))

centena = numero-(milhar*1000)
centena = math.floor(centena/100)
print('A centena do seu numero é: {}'.format(centena))

dezena=numero-((milhar*1000)+(centena*100))
dezena=math.floor(dezena/10)
print('A dezena do seu numero é: {}'.format(dezena))

unidade=math.floor(numero%10)
print('A unidade do seu número é: {}'.format(unidade))




