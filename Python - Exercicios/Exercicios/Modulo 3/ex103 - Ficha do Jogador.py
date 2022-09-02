# Criar uma funçao ficha()
# Recebe os parametros opcionais:
# 1- nome de um jogador
# 2- quantos gols ele marcou
# Mostrar ficha, mesmo que nao tenha sido informado.

def linha():
    """
    ->Cria uma linha divisória
    """
    print('-' * 30)


def ficha(nome='', gols=''):
    if nome == '' or gols == '':
        if nome == '' and gols == '':
            print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
        elif nome=='':
            print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
        elif gols=='':
            print(f'O jogador {nome} fez 0 gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
linha()
ficha(str(input('Nome do Jogador: ')),
      str(input('Número de Gols: ')))
linha()
