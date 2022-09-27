# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

import time

distancia = int(input('Digite a distancia em Km: '))

print('Calculando..')
time.sleep(2)

# Simplificado
print('SIMPLIFICADO: o valor da passagem será: R${:.2f}'.format(distancia*0.5) if distancia <= 200 else 'SIMPLIFICADO: O valor da passagem será: R${:.2f}'.format(distancia*0.45))


# Composto
if distancia <= 200:
    print('COMPOSTO: O valor da passagem será: R${:.2f}'.format(distancia*0.5))
else:
    print('COMPOSTO: O valor da passagem será: R${:.2f}'.format(distancia*0.45))