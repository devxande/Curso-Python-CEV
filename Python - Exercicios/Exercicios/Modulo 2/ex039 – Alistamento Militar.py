# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from time import sleep
from datetime import date

atual = date.today().year
nascimento = int(input('-=-'*10 + '\n***PROGRAMA INICIADO***\n'
                                  'Digite sua data de nascimento para analise:\n'
                                  '-> '))
print('-=-'*20 + '\n WAITING... WAITING...\n'+'-=-'*20)
sleep(1)

idade = atual-nascimento
if idade<18:
    print('Você ainda não pode se alistar!\n'
          'Anos que faltam: {}'.format(18-idade))
elif idade==18:
    print('''Chegou sua vez de servir ao Brasil!
    Aliste-se já! Ano de nascimento: {}'''.format(nascimento))
else:
    print('Já passou o seu tempo de alistamento!\n'
          'Apresente-se a unidade mais proxima para regularização.\n'
          'Anos passados: {}'.format(idade-18))