# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
cont=0
for c in range(1, 500, 2):
    multi = c % 3
    if multi == 0:
        print(c,end=' ')
        soma += c
        cont+=1
print(f'\nA soma de todos os números é {soma}\nQuantidade de números divisiveis por 3: {cont}')
