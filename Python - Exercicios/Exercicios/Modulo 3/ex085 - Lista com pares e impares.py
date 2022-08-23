# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], [], []]
dados = 0
for cont in range(0, 7):
    dados = int(input('Digite um valor: '))
    valores[2].append(dados)
    if dados % 2 == 0:
        valores[0].append(dados)
    else:
        valores[1].append(dados)

valores[0].sort(), valores[1].sort(), valores[2].sort()

print(f'''\n{20 * "*"}
Lis de valores completa: {valores[2]}
Lista de valores pares: {valores[0]}
Lista de valores impares: {valores[1]}''')
