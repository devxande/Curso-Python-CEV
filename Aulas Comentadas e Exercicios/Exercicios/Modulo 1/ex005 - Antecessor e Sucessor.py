# Exercício Python 5: Faça um programa que leia um número Inteiro
# e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um valor: '))
antecessor = n1-1
sucessor = n1+1

print('Numero digitado é {} \nSeu antec essor é {} e seu sucessor é {}'.format(n1 , antecessor , sucessor))
#print('Numero digitado é {} \nSeu antec essor é {} e seu sucessor é {}'.format(n1 , (n1-1) , (n1+1))
