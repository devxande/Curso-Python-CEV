# Exercício Python 8: Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite quantos metros para conversão: '))
centimetros = metro*100
milimetros = metro*1000

print('{} metros é igual a {} centimetros e {} milimetros'.format(metro , centimetros , milimetros))