# criar funçao area()
# Recebe as dimensões de um terreno retangular (largura/compr.)
# mostrar area do terreno.

def titulo(msg):
    print(f'''{"-=-"*10}
{msg:^30}
{"---"*10}''')


def area(a, b):
    tam = a * b
    print(f'A área de um terreno {a}x{b} é de {tam}m².')


# PROGRAMA PRINCIPAL
titulo('Controle de Terrenos')
area(int(input('Largura (m): ')), int(input('Comprimento (m): ')))
