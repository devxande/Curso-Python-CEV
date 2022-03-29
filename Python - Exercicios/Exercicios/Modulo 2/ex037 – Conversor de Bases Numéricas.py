# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

inteiro = int(input('Programa iniciado!\n'
                    'Digite um valor para conversão: '))
opcao = float(input('''Escolha uma das opções para conversão
1-Binário
2-Octal
3-\033[33mHexa\033[m
Digite aqui:'''))
print('====' * 10, '\nProcessando..\n', '====' * 10)
if opcao == 1:
    print(bin(inteiro))
elif opcao == 2:
    print(oct(inteiro)[2:])
else:
    print(hex(inteiro)[2:])
