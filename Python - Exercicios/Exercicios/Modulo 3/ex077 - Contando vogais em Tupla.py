# Tupla com varias palavras, sem acento;
# Mostrar para cada palavra quantidade de vogais.
from random import randint
palavras = (
    'Preto', 'Vermelho', 'Verde', 'Amarelho',
    'Azul', 'Rosa', 'Ciano', 'Cinza',
    'Branco', 'Prata', 'Inooth', 'Fone',
    'Quebrado','Vender', 'Camera'
)
for c in range(0,len(palavras)):
    vogais = palavras[c].lower().count("a")
    vogais += palavras[c].lower().count("e")
    vogais += palavras[c].lower().count("i")
    vogais += palavras[c].lower().count("o")
    vogais += palavras[c].lower().count("u")
    print(f'A palavra ->\033[3{randint(1,8)}m{palavras[c]:^15}\033[m<- tem: {vogais} vogais! ')

print('PAçoca')