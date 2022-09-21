# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.

from libPorque.arquivo import arquivo
from libPorque.interface import interface

# Programa Principal
arq = 'cursoemvideo.txt'
if not arquivo.arquivoExiste(arq):
    print('O arquivo não foi encontrado...')
    arquivo.criarArquivo(arq)
while True:
    resposta = interface.mostrarMenu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opcao de listar o conteudo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        # Opcao de cadastrar uma nova pessoa.
        interface.titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opcao de sair do programa.
        interface.titulo('\033[33mSaindo do sistema... Fim.\033[m')
        break
    else:
        print('\033[31mErro!!! Digite uma opção valida.\n\033[m')
