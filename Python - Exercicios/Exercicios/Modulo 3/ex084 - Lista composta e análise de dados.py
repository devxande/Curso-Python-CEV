#Ler nome e peso e guardar na lista
#Quantas pessoas cadastradas
#listagem com as pessoas mais pesadas
#listagem com pessoas mais leves
dados = []
pessoas = []
contadorPessoas = 0
while True:
    dados.append(str(input('Digite o NOME: ')))
    dados.append(str(input('Digite o PESO: ')))
    pessoas.append(dados[:])
    dados.clear()
    contadorPessoas+=1

    #SAIR
    sair = ' '
    while sair not in 'SN':
        sair=str(input('Adicionar nova pessoa? [S/N]')).upper().strip()[0]
    if sair == 'N':

        break

print(f'''Número de pessoas cadastradas: {contadorPessoas}O MAIOR peso  foi de''')