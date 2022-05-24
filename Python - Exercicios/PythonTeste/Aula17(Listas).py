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

#Cria uma ligação
a = [2,3,4,7]
b = [8,10,20]
b[2]=8
print(a,b)
b = a[:]









