#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1,10),
randint(1,10),
randint(1,10),
randint(1,10),
randint(1,10))
maior=menor=0
print('A listagem dos valores gerados é: ', end='')
for c in range (0,5):
    print(numeros[c], end=',') if c !=4 else print(numeros[c], end='.')
    # if c==0:
    #     maior=numeros[c]
    #     menor = numeros[c]
    # else:
    #     if numeros[c]>maior:
    #         maior=numeros[c]
    #     if numeros[c]<menor:
    #         menor=numeros[c]
# print(f'''\nO maior valor é o: {maior}
# O menor valor é o: {menor}''')

# Posso usar a forma de cima para saber o maior e menor valor,
# ou o comando max e min.
print(f'''\nO maior valor é o: {max(numeros)}
O menor valor é o: {min(numeros)}''')

