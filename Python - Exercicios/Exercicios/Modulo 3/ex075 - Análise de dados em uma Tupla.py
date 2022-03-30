# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# cont=0
# valor = [a,b,c,d]
# while cont != 5:
#     valor[cont]=int(input('Digite um valor: '))
#     cont+=1
# valor=(
#     input(),
#     input
# )
# print(valor)
# for c in range(0,4):
#     valor[c]=int(input(f'Digite o {c+1}º valor: '))

# Resolução:
num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: '))
       )
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 aparece na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')
