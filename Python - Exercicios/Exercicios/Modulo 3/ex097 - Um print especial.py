# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.


def titulo(msg):
    tam = len(msg)+4
    print(f'''{"*" * tam}
  {msg}
{"=" * tam}''')


titulo(str(input('Digite sua frase para titulo: ')))
