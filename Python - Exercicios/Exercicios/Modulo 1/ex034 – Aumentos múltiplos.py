# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep
from datetime import date

cores = {
    'azul': '\033[34m',
    'vermelho': '\033[31m',
    'amarelho': '\033[33m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'limpa': '\033[m'
}

salario = float(input('Digite seu salário: '))

print('-=-' * 20, '\nProcessando...', '\n', '-=-' * 20)
sleep(0)

print('***em Brasília, {}{}/{}/{}{}***'.format(cores['azul'], date.today().day, date.today().month, date.today().year,
                                               cores['limpa']))

if salario > 1250:
    print('Seu salário atual: R${} \nAumentou para: {}R${}'.format(salario, cores['vermelho'],
                                                                   (salario * 0.10) + salario))
else:
    print('Seu salário atual: R${:.2f} \nAumentou para: R${:.2f}'.format(salario, (salario * 0.15) + salario))
