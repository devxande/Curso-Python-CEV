def titulo(msg):
    tam = len(msg) + 20
    print(f'''\033[31;40m{"*" * tam}\033[m
\033[31;40m{msg.center(tam)}\033[m
\033[31;40m{"=" * tam}\033[m''')


def aumentar(numero=0, porcent=0, verificar=False):
    res = numero + (numero * porcent / 100)
    # Todas as formas de veririficar são iguais.
    if verificar is True:
        return moeda(res)
    else:
        return res


def diminuir(numero=0, porcent=0, verificar=False):
    res = numero - (numero * porcent / 100)
    # Todas as formas de veririficar são iguais.
    return res if verificar is False else moeda(res)


def dobro(numero=0, verificar=False):
    res = numero * 2
    # Todas as formas de veririficar são iguais.
    return res if verificar is False else moeda(res)


def metade(numero=0, verificar=False):
    res = numero / 2
    # Todas as formas de veririficar são iguais.
    if verificar is True:
        return moeda(res)
    else:
        return res


def moeda(num=0.0, valor='R$'):
    return f'{valor}{num:>8.2f}'.replace('.', ',')


def resumo(num=0, porcAumentar=0, porcDiminuir=0):
    titulo('RESUMO DO VALOR')
    print(f'''Preço Analisado: \t{moeda(num)}
Dobro do preço: \t{dobro(num, True)}
Metade do preço: \t{metade(num, True)}
{porcAumentar}% de aumento: \t{aumentar(num, porcAumentar, True)}
{porcDiminuir}% de redução: \t{diminuir(num, porcDiminuir, True)}
    ''')
