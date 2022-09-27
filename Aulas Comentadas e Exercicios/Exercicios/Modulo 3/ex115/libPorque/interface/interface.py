
def leiaInt(msg):
    """
    -> Verifica se é inteiro
    :return:Mostra o número inteiro corretamente.
    """
    while True:
        try:
            txt = int(input(msg))
        except (ValueError, TypeError) as erro:
            print(f'''\033[31mERRO! Tipo de dados incorreto.\033[m
ERRO NO SISTEMA ({erro})
Digite novamente...\n''')
            continue
        except KeyboardInterrupt:
            print(f'''\033[31mUsuário preferiu não digitar esse número.\033[m''')
            return 0
        else:
            return txt


def linha(tam=42):
    return '-' * tam


def titulo(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def mostrarMenu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao
