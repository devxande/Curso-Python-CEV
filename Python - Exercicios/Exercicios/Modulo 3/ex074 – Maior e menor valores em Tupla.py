#gerar 5 numeros aleatorios e colocar na tupla
#mostrar listagem dos numeros gerado
# e mostrar o maior e menor.

from random import randint
numeros = (randint(1,1000),
randint(1,1000),
randint(1,1000),
randint(1,1000),
randint(1,1000))
c=maior=menor=0
print('A listagem dos valores gerados é: ', end='')
for c in range (c,5):
    print(numeros[c], end=',') if c !=4 else print(numeros[c], end='.')
    if c==0:
        maior=numeros[c]
        menor = numeros[c]
    else:
        if numeros[c]>maior:
            maior=numeros[c]
        if numeros[c]<menor:
            menor=numeros[c]
    c+=1
print(f'''\nO maior valor é o: {maior}
O menor valor é o: {menor}''')

