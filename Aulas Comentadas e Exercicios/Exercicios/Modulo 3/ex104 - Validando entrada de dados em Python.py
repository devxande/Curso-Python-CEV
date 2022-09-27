# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘
# a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def linha():
    """
    ->Cria uma linha divisória
    """
    print('-' * 30)


def leiaInt(txt):
    """
    -> Verifica se é inteiro
    :param txt: Algum valor para verificar
    :return:Mostra o número inteiro corretamente.
    """
    while not txt.isnumeric():
        txt = str(input('Digite um valor: '))
        if txt.isnumeric():
            return txt
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal

n = leiaInt('Digite um número: ')
linha()
print(f'\033[34mVocê acabou de digitar o número {n}\033[m')
