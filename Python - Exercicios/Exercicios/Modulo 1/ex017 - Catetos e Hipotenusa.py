# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
catOposto=float(input('Digite o cateto oposto: '))
catAdjacente=float(input('Digite o cateto adjacente: '))
print('Os catetos {} e {} tem o valor da hipotenusa {:.2f}'.format(catAdjacente, catOposto , hypot(catAdjacente,catOposto)))
hipo=(catOposto ** 2 + catAdjacente ** 2) ** 0.5
print('Os catetos {} e {} tem o valor da hipotenusa {:.2f}'.format(catOposto,catAdjacente,hipo))



