# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

n = input('Digite um algo: ')
print(type(n))
print("Valor digital é alpha?",n.isalpha())
print("Valor digital é numero?",n.isnumeric())
print("Valor digital é maiusculo?",n.isupper())

