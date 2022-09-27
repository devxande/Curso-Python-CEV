# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    """
    -> Verifica se é inteiro
    :return:Mostra o número inteiro corretamente.
    """
    txt = 0
    verificador = False
    while verificador is not True:
        try:
            txt = int(input('Digite um valor: '))
        except (ValueError, TypeError) as erro:
            print(f'''\033[31mERRO! Tipo de dados incorreto.\033[m
ERRO NO SISTEMA ({erro})
Digite novamente...\n''')
        except KeyboardInterrupt:
            print(f'''\033[31mUsuário preferiu não digitar esse número.\033[m''')
            return txt
        else:
            print('Numero Inteiro Verificado!')
            verificador = True
    return txt


def leiaFloat():
    """
    -> Verifica se é Float
    :return:Mostra o número inteiro corretamente.
    """
    txt = 0
    verificador = False

    while verificador is not True:
        try:
            txt = float(input('Digite um valor: '))
        except (ValueError, TypeError) as erro:
            print(f'''\033[31mERRO! Tipo de dados incorreto.\033[m
ERRO NO SISTEMA ({erro})
Digite novamente...\n''')
        except KeyboardInterrupt:
            print(f'''\033[31mUsuário preferiu não digitar esse número.\033[m''')
            return txt
        else:
            print('Numero Real Verificado!')
            verificador = True
    return txt


# Programa Principal
print(f'O valor inteiro digitado foi {leiaInt()} e o real foi {leiaFloat()}')
