# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

celsius = (float(input('Digite a temperatura em graus ºC: ')))
fahren = (celsius*9/5)+32
print('O valor de {} ºC convertido é {} ºF'.format(celsius , fahren))