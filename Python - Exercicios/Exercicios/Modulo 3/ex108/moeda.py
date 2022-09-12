def aumentar(numero=0, porcent=0):
    res = numero + (numero * porcent / 100)
    return res


def diminuir(numero=0, porcent=0):
    res = numero - (numero * porcent / 100)
    return res


def dobro(numero=0):
    res = numero * 2
    return res


def metade(numero=0):
    res = numero / 2
    return res


def moeda(num=0, valor='R$'):
    return f'{valor}{num:.2f}'.replace('.', ',')
