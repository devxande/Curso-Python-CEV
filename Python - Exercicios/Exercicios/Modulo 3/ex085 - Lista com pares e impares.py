#Ler sete valores, lista unica
#Manter separado os valores pares e impares
#Mostrar ordem crescente

valores = [[],[],[]]
dados = 0
for cont in range(0,3):
    dados = int(input('Digite um valor: '))
    valores[2].append(dados)
    if dados % 2 == 0:
        valores[0].append(dados)
    else:
        valores[1].append(dados)

valores[0].sort(), valores[1].sort(),valores[2].sort()

print(f'''\n************
Lis de valores completa: {valores[2]}
Lista de valores pares: {valores[0]}
Lista de valores impares: {valores[1]}''')
