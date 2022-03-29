# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite o nome da cidade:'))
nome=nome.lower()
print(nome.find('santo'))
print('Se aparecer 0 tem o nome Santo, se aparecer -1, não tem.')