# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior
# e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

sair = 'n'
soma = media = maior = menor = cont = 0
while sair in 'Nn':
    num = int(input('Digite um valor: '))

    # Maior e Menor número.
    if maior == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    cont += 1
    media = soma / cont
    print(f'''{"-=" * 10}
A média dos {cont:.2f} valores é: {media}
O maior valor é: {maior}
O menor valor é: {menor}
{"-=" * 10}\n''')
    sair = str(input('Gostaria de finalizar? [S/N]: ').upper().strip()[0])
print('Programa Finalizado!')
