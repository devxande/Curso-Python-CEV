# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.


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
