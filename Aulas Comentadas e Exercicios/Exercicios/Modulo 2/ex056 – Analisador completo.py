# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

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
}  #
nome = [0, 1, 2]
idade = [0, 1, 2]
sexo = [0, 1, 2]
media = 0
novas = 0
velho = [0, 1]

for c in range(0, 3):
    print(38 * '{}={}'.format(cores['purple'], cores['clear']))
    nome[c] = str(input('Nome: '))
    idade[c] = int(input('Idade: '))
    sexo[c] = int(input('[ 1 ]-Masculino [ 2 ]-Feminino --> '))
    media += idade[c]
    if sexo[c] == 1:
        if idade[c] > velho[1]:
            velho[0] = nome[c]
            velho[1] = idade[c]
    else:
        if idade[c] < 20:
            novas += 1

print(f'{cores["purpleFundo"]}{" INFORMAÇÕES ":=^40}{cores["clear"]}' +
      f'\n{velho[0]} é o homem mais velho e tem {velho[1]} anos!' +
      f'\nIdade média do grupo: {media/3:.0f} anos!' +
      f'\nMulheres com menos de 20 anos: {novas}')
