#Primeiro Exemplo:
dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = list()
pessoas.append(dados[:])
#Colocar o [:] para copiar a lista!!!

#Segundo Exemplo:
pessoas = [['Pedro',25],['Maria',19],['Joao',32]]

#Testes:
print(pessoas)
print(pessoas[0][0])
print(pessoas[2][0])
print(pessoas[1])

print('\n*** Divisoria 1 ****')
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

print('\n*** Divisoria 2 ****')
galera = [['Joao',19],['Ana',33],['Joaquin',13],['Maria',45]]
print(galera)

print('\n*** Divisoria 3 ****')
for p in galera:
    print(p)
    print(f'O nome {p[0]} e sua idade {p[1]}')

print('\n*** Divisoria 4 ****')
galera = []
dado = []

#Ler os dados
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade.')