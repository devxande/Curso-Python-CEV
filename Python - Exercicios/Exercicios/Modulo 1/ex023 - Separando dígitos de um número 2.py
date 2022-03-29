# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# com string

numero = str(input('Digite um valor de 0 a 9999:'))
milhar = numero[0]
centena = numero[1]
dezena = [2]
unidade = [3]
print('Milhar: {} , Centena: {} , Dezena: {} , Unidade: {}'.format(milhar, centena, dezena, unidade))
