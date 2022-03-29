#Exercício Python 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O angulo {} tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(angulo, sen, cos, tan))
