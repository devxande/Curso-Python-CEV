# Exercício Python 26: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase:')).strip()
print('A letra "A" aparece: {} vezes'.format(frase.lower().count('a')))
print('Aparece primeiro na posição {}'.format(frase.lower().find('a')+1))
print('Aparece ultimo na posição {}'.format(frase.lower().rfind('a')+1))
