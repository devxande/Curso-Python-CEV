# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar s
# e o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from time import *

contIdade = contMasc = contMulheres = convertInt=0
while True:
    while True:
        idade = str(input('Digite sua idade: '))
        if str.isnumeric(idade):
            convertInt=int(idade)
            break

    sexo=' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    # while True:
    #     sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    #     if sexo == 'M' or sexo == 'F':
    #         break
    #+18 anos
    if convertInt >= 18:
        contIdade += 1
    #qntd masculino
    if sexo == 'M':
        contMasc += 1
    #Mulher 20+
    if convertInt > 20 and sexo == 'F':
        contMulheres += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Adicionar mais um? [S/N]').strip().upper()[0])
    if escolha == 'N':
        break

print(f'''{10*"="}
Qntd de pessoas MAIORES de 18 anos: {contIdade}
Qntd de pessoas SEXO MASCULINO: {contMasc}
Qntd de mulheres MAIORES que 20 anos: {contMulheres}
{10*"="}
''')
