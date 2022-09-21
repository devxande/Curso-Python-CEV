from ..interface.interface import *


def arquivoExiste(nome):
    try:
        # open() = Abre um arquivo
        # rt = Read Text
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        # wt = Write Text; + = caso nao exista, ele cria.
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro na abertura do arquivo.')
        a.close()
    else:
        titulo('PESSOAS CADASTRADAS')
        for linhaArquivo in a:
            dado = linhaArquivo.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except FileNotFoundError:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except FileExistsError:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado ao sistema.\n')
            a.close()
