lanche=['Hamburg','Suco','Pizza','Sorvete']
# Adicionar elemento a lista (unica forma)
lanche.append('Coockie')
print(lanche)

#Adicionar elemento em certa posição (Anda uma posição a frente)
lanche.insert(0,'HotDog')
print(lanche)

#Apagar elementos no indice
#del lanche[3]
#ou remover no indice, ele remove o primeiro elemento, se remover um inexistente dá erro.
#lanche.pop[3]
#ou para remover o valor especifico
#Os valores são reposicionados
#caso não haja o valor para remover, utilizar o IF.
#lanche.remove['Pizza']
#caso não haja o valor para remover, utilizar o IF.
if 'pizza' in lanche:
    lanche.remove['pizza']

#Declarar uma lista com range
valores = list(range(4,11))

print('\n*************\n',valores)
#Ordenar .sort
#Ordernar inverso
valores.sort(reverse=True)
print('\n*************\n',valores,'\n*******\n')

valores.insert(0,'oiiii')
#Quantidade de valores
print(f'Essa lista tem {len(valores)} valores.','\n********\n',valores)

valores.pop(0)
print(valores)

if 4 in valores:
    valores.remove(4)
    print('Número 4 foi removido.')
else:
    print('Número 4 não encontrado.')
print('\n**************\n')

num = []
num.append(5)
num.append(9)
num.append(4)
num.sort(reverse=True)
for c, n in enumerate(num):
    print(f'na posição {c} encontrei o valor {n}')
print('Cheguei no fim. \n********\n')

teste = []
#for cont in range (0,5):
    #teste.append(int(input('Digite um valor: ')))
#print('\n********\n')

num = [2,5,9,1]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
print(num)
print(f"Essa lista tem {len(num)} elementos.\n")
if 4 in num:
    num.remove(4)
else:
    print("nao tem o valor 4")
#num.pop(2)
print(num)
print("**************\n")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0,1):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    print(f'Na posição: {c} encontrei o valor {v}')

print('*************\n')

#Ligação de uma lista com outra.
a = [1,2,3,4]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Copia de uma lista. [:] significa todos os elementos do teste1.
teste1 = [1,2,3,4]
teste2 = teste1[:]
teste2[2] = 8
print(f'Lista teste1: {teste1}')
print(f'Lista teste2: {teste2}')









