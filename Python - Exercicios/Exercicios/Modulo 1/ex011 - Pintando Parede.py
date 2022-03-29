# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('Sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(altura , largura , area))
print('A quantidade de tinta para a área de {} são de {} litros'.format(area, tinta))
