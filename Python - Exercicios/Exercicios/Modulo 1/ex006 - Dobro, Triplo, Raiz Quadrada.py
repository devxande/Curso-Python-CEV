# Exercício Python 006: Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.

n1 = float(input('Digite um valor: '))
d = n1*2
t = n1*3
rq = n1**0.5

print('Dobro do valor: {:.0f}\nTriplo do valor: {:.0f}\nRaiz quadrada do valor: {:.3f}'.format(d , t , rq))
#pow (n1, (1/2)) tb calcula raiz quadrada.