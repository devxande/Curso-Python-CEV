# criar funçao escreva()
# Recebe um texto qualquer
# mostrar com tamanho adaptavel

def titulo(msg):
    print(f'''{"-=-" * len(msg)}
{msg}
{"---" * len(msg)}''')


titulo(str(input('Digite sua frase para titulo: ')))
