# Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#.strip().upper() - Tira os espaços laterais e coloca tudo em maiusculo.
frase = str(input('Digite uma frase: ')).strip().upper()
#.split() - Divide a fra em lista e bota na variavel.
palavras = frase.split()
# ''.join(palavras) - funçao de adicionar ao entre os espaços,
# ele adiciona nada, ou seja, remove os espaços.
junto = ''.join(palavras)
inverso = ''

#len(junto) mostra a qntidade de letras sem espaços e vai até -1.
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(f'O inverso de {junto} é {inverso}')