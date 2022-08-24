# Iniciar Dicionario
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

# Adicionar elementos
dados['sexo'] = 'M'
print(dados['sexo'])

# Outro exemplo
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'direto': 'George Lucas'
}

print(30*'*','\n')

#Pega os valores DENTRO de cada posição: joao,10,M
print(filme.values())
#Pega o nome de cada posição: nome,idade,sexo
print(filme.keys())
#Pega ambos values e keys.
print(filme.items())

print(30*'*','\n')

#Para cada keys e value em items, ele vai fazer um print.
for k,v in filme.items():
    print(f'O {k} é {v}')

#Exemplos
print(30*'*','\n')

pessoas={'nome':'Gustavo','sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k, v in pessoas.items():
    print(f'{k} = {v}')
#Adicionar nova key e value
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

#Deletando uma key e value.
del pessoas ['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

#Exemplo 2
print(30*'*','\n')

#Lista com Dicionarios
brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])

brasil.clear()

#Exemplo 3
print(30*'*','\n')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')
