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


def moeda(num=0, valor='R$'):
    return f'{valor}{num:.2f}'.replace('.', ',')
