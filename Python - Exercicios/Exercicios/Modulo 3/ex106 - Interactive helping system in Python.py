def titulo(msg):
    tam = len(msg) + 4
    print(f'''\033[31;40m{"*" * tam}
  {msg}
{"=" * tam}\033[m''')


def pyHELP():
    sair = ' '
    while sair not in 'FIM':
        titulo('SISTEMA DE AJUDA PyHELP')
        help(str(input('Função ou Biblioteca > ')))
        sair = str(input('Digite "FIM" para encerrar o programa: ')).upper()[0]
        if sair == 'FIM':
            break


# Código Principal
pyHELP()
