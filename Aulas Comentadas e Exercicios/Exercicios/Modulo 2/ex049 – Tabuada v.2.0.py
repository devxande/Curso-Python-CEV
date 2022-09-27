# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num1 = int(input('\033[1;32m**Tabuada do Xandon**\033[m'
                 '\nDigite um número inteiro: '))
for c in range(0, 10 + 1):
    print(f'{num1} x {c} = \033[32m{num1 * c}\033[m')
