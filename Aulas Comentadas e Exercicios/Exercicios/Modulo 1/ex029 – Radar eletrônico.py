# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

velo = int(input('Digite a velocidade do carro em Km/h: '))

print('Processando...')
sleep(3)

# Simplificada
print('SIMPLIFICADA: Não foi multado, velocidade permitida.' if velo <= 80 else 'SIMPLIFICADA: Velocidade não permitida. Você foi multado no valor de R${}'.format((velo-80)*7))

# Composta
if velo <= 80:
    print('COMPOSTA: Não foi multado.')
else:
    print('COMPOSTA: Você foi multado no valor de {:.2f}'.format((velo-80)*7))
