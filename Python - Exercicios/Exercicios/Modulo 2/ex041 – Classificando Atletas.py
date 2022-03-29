# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from time import sleep

cores = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'blue': '\033[1;34m',
    'purple': '\033[1;34m',
    'clear': '\033[m'
}
ano = int(input('-=-' * 10 + '\n{}**PROGRAMA INICIADO**{}\n'.format(cores['red'], cores['clear'])
                + 'Digite sua data de {}nascimento:{} '.format('\033[4m', cores['clear'])))

print('-=-' * 10 + '{}\nCarregando..\n{}'.format(cores['blue'], cores['clear']) + '-=-' * 10)
sleep(1)

idade = 2022 - ano
if ano > 2022 or idade < 0:
    print('{}Ano indisponível, tente novamente.{}'.format(cores['red'], cores['clear']))
else:
    if idade <= 9:
        print('{} anos - {}Competidor Mirim.'.format(idade, cores['yellow']))
    elif 9 < idade <= 14:
        print('{} anos - {}Competidor Infantil.'.format(idade, cores['green']))
    elif 14 < idade <= 19:
        print('{} anos - {}Competidor Júnior.'.format(idade, cores['purple']))
    elif 19 < idade <= 20:
        print('{} anos - {}Competidor Senior.'.format(idade, cores['blue']))
    else:
        print('{} anos - {}Competidor Master.'.format(idade, cores['red']))
