# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python
# e como utilizá-lo com parâmetros simples e múltiplos.

# EXEMPLO 1
def lin():
    print(f'{"-=-" * 20}')


lin()
print('SISTEMA DE ALUNOS')
lin()
lin()
print('CADASTRO DE FUNCIONARIO')
lin()


# EXEMPLO 2
def mensagem(msg):
    print(f'{"-=-" * 20}')
    print(msg)
    print(f'{"-=-" * 20}')


mensagem('SISTEMA DE ALUNOS')


# EXEMPLO 3
def titulo(txt):
    print(f'{"-=-" * 20}')
    print(txt)
    print(f'{"-=-" * 20}')


titulo(' CURSO EM VIDEO ')


# EXEMPLO 4
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# PROGRAMA PRINCIPAL
soma(4, 5)
soma(b=4, a=5)


def contador(*num):
    print(num)
    tam = len(num)
    for valor in num:
        print(f'Os valores são {valor}, total de {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# EXEMPLO 5
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
