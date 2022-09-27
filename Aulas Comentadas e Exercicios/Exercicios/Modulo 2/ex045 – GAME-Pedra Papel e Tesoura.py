# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import choice
import emoji

cores = {
    'lateral': '\033[m''\033[7;1;40m''*''\033[m',
    'star': '\033[7;1;40m',
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'blue': '\033[1;34m',
    'purple': '\033[1;35m',
    'purpleFundo': '\033[35;1;40m',
    'blackFundo': '\033[;1;40m',
    'bold': '\033[1m',
    'clear': '\033[m',
}  # CORES

print(f'{cores["star"]}{" GAME DO XANDÃO ":*^40}{cores["clear"]}'
      f"\n{cores['purpleFundo']}{'Você está no game JOOO KEEEN POOO!':^40}{cores['clear']}"
      f'\n{cores["star"]}{"":*^40}{cores["clear"]}')  # TITULO

escolha = int(
    input(f'{cores["lateral"] + cores["purpleFundo"]}{"Escolha uma das opções":^38}{cores["lateral"]}' +
          f'\n{cores["lateral"] + cores["blackFundo"]}{"[ 1 ] - PEDRA":^38}{cores["lateral"]}' +
          f'\n{cores["lateral"] + cores["blackFundo"]}{"[ 2 ] - PAPEL":^38}{cores["lateral"]}' +
          f'\n{cores["lateral"] + cores["blackFundo"]}{" [ 3 ] - TESOURA":^38}{cores["lateral"]}' +
          f'\n{cores["lateral"] * 40}' +
          f'\n{cores["red"]}{" Qual é a sua jogada? ":>31}{cores["clear"]}'))

if 1 <= escolha <= 3:
    print(emoji.emojize(":heart:" * 17, use_aliases=True))
    print(f'{"JO":^38}')
    sleep(0.7)
    print(f'{"KEN":^38}')
    sleep(0.7)
    print(f'{" PO!!! ":^38}')
    print(emoji.emojize(":heart:" * 17, use_aliases=True))
    sleep(0.5)
    print(cores["lateral"] * 40)

sorteio = choice([1, 2, 3])
if escolha == 1:
    if sorteio == 3:
        print(f'{"Você GANHOU!!!":^38}\n{"Você:Pedra  vs.  Robô:Tesoura":^38}\n{"Logo a Pedra ganha!":^38}')
    elif sorteio == 2:
        print(f'{"Você PERDEU!!":^38}\n{"Você:Pedra  vs.  Robô:Papel":^38}\n{"Logo a Pedra perde!":^38}')
    else:
        print(f'{"Deu EMPATE!!":^38}\n{"Você:Pedra  vs.  Robô:Pedra":^38}\n{"AI QUE GAATTUMMM":^38}')
elif escolha == 2:
    if sorteio == 1:
        print(f'{"Você GANHOU!!!":^38}\n{"Você:Papel  vs.  Robô:Pedra":^38}\n{"Logo o Papel ganha!":^38}')
    elif sorteio == 3:
        print(f'{"Você PERDEU!!!":^38}\n{"Você:Papel  vs.  Robô:Tesoura":^38}\n{"Logo o Papel perde!":^38}')
    else:
        print(f'{"Deu EMPATE!!!":^38}\n{"Você:Papel  vs.  Robô:Papel":^38}\n{"HAA HAA HA MIEUUH":^38}')
elif escolha == 3:
    if sorteio == 2:
        print(f'{"Você GANHOU!!!":^38}\n{"Você:Tesoura  vs.  Robô:Papel":^38}\n{"Logo a Tesoura ganha!":^38}')
    elif sorteio == 1:
        print(f'{"Você PERDEU!!!":^38}\n{"Você:Tesoura  vs.  Robô:Pedra":^38}\n{"Logo a Tesoura perde!":^38}')
    else:
        print(f'{"Deu EMPATE!!!":^38}\n{"Você:Tesoura  vs.  Robô:Tesoura":^38}\n{"kiko kiko raa raa raa":^38}')
else:
    print(cores["lateral"] * 40)
    print(
        f'{cores["red"]}{"**VOCÊ É IDIOTA? OPÇÃO INVALIDA, QUERIDO**":^38}{cores["clear"]}\033[1m{"PROGRAMA ENCERRANDO..":^38}'), \
    sleep(1)

print(cores["lateral"] * 40)
print(
    f'\n{cores["purple"]}{"**REINICIE E JOGUE NOVAMENTE**":^38}{cores["clear"]}\n\033[1m{"PROGRAMA ENCERRANDO..":^38}')
sleep(1)
