# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

n1 = float(input('Digite quantos reais tem: R$ '))
dolar = n1/6
print('Seu dinheiro de R${:.2f} convertido para dolar é: US${:.3f}'.format(n1 , dolar))