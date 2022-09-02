# Criar uma funçao leiaInt()
# Funciona similar ao input()
# Aceita apenas valor numerico

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
