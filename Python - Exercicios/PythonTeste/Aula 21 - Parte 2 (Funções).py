# Nessa aula, vamos continuar nossos estudos de funções em Python,
# aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções,
# argumentos opcionais para dar mais dinamismo em funções Python,
# escopo de variáveis e retorno de resultados.

# Descrição das funções
# exemplo
# help(print)
# print('olá, mundo')

# exemplo 2
# print(print.__doc__)

# Docstring
# colocar abaixo do def """""", irá aparecer no help()
def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: final da contgem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}')
        c += p
    print('fim')


# Parametros Opcionais
# caso não seja atribuido nenhum valor ao chamar a funçao
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


# Escopo de Variável
# a variavel 'n' funciona na função por ser global.
# a variavel 'x' não funciona fora da função, ela é local
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# A funcao cria uma variavel com mesmo nome local,
# para editar a variavel global dentro da funcao
# é necessário colocar global "variavel"
def funcao():
    global n1
    n1 = 4
    print(f'n1 dentro vale {n1}')


# Retorno de Valores
# uteis para personalização dos resultados
def somarReturn(a=0, b=0, c=0):
    s = a + b + c
    return s


# Codigo principal
help(contador)
contador(0, 100, 100)

help(somar)
somar(3, 2, 5)
# não dá erro.
somar(8, 4)
somar()

print('\n')
n = 2
print(f'No programa principal,n vale {n}')
teste()

print()
n1 = 2
funcao()
print(f'n1 fora vale {n1}')

print()
r1 = somarReturn(1, 2, 3)
r2 = somarReturn(3, 2)
r3 = somarReturn(2)

print(f'Os resultados foram {r1}, {r2} e {r3}')
