# Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do Fatorial de um número n.
    """
    f = 1
    if show == True:
        print(num, end=' ')
        for c in range(num, 1, -1):
            f *= c
            print(f'x {c - 1}', end=' ')
        print(f'= {f}')
    else:
        for c in range(num, 1, -1):
            f *= c
        print(f)


def linha():
    """
    ->Cria uma linha divisória
    """
    print('-' * 30)


# Programa Principal
linha()
num = int(input('Valor para calcular: '))
opcao = ' '
while opcao not in 'SN':
    opcao = str(input('Visualizar calculo? [S/N]')).upper()[0]
if opcao == 'S':
    fatorial(num, show=True)
if opcao == 'N':
    fatorial(num)
linha()
