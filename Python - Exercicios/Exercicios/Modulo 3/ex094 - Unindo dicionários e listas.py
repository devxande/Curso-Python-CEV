# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoa = {}
listaPessoas = []
sexoVerificar = ' '
idadeTotal = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    sexoVerificar = ' '
    while sexoVerificar not in 'MF':
        sexoVerificar = str(input('Digite o sexo: ')).upper().strip()[0]
    pessoa['sexo'] = sexoVerificar
    pessoa['idade'] = float(input('Digite a idade: '))
    idadeTotal += pessoa['idade']
    listaPessoas.append(pessoa.copy())

    # Sair
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar nova pessoa? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break

# Pessoas Cadastradas
print(f'\n{"-=-" * 15}')
print(f'A) Quantidade de Pessoas Cadastradas: {len(listaPessoas)}\n')

# Media de idade

print(f'B) A media das idades é -> {idadeTotal / len(listaPessoas):5.2f} anos\n')

# Lista com mulheres
print(f'C) As Mulheres Cadastradas foram: ', end='')
for pos in listaPessoas:
    if pos['sexo'] == 'F':
        print(f'{pos["nome"]}', end='; ')
print()
# Lista de pessoas acima da media
print(f'\nD) Idades acima da MÉDIA: ')
for pos in listaPessoas:
    if pos['idade'] > (idadeTotal / len(listaPessoas)):
        for k, v in pos.items():
            print(f'{k} = {v}; ', end='')
        print('')
print('-=-' * 15)
