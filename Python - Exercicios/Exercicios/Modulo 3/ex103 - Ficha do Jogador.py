# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
def linha():
    """
    ->Cria uma linha divisória
    """
    print('-' * 30)


def ficha(nome='', gols=''):
    if not gols.isnumeric():
        gols = '0'
    if nome == '' or gols == '':
        if nome == '' and gols == '':
            print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
        elif nome == '':
            print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
        elif gols == '':
            print(f'O jogador {nome} fez 0 gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
linha()
ficha(str(input('Nome do Jogador: ')),
      str(input('Número de Gols: ')))
linha()
