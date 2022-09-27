# Exercício Python 12: Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço normal: R$'))
print('O produto com desconto de 5% fica por:{:.2f}'.format(preco-(preco*0.05)))