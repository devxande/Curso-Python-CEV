# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

escolha = num = comp = win = 0
print(f'''{20*"¨"}
JOGO DO IMPAR OU PAR
  criador: Xandon
{20*"¨"}''')
while True:
    escolha = str(input('Escolha entre PAR ou IMPAR [P/I]: ').upper().strip()[0])
    num = int(input('Escolhar um número para o jogo: '))
    comp = randint(1, 10)
    if escolha == 'P':
        if (num + comp) % 2 == 0:
            print(f'Você:{num}\nComputador:{comp}\nResultado:{num + comp}\nDeu PAR!! Você \033[36mGanhou\033[m')
            win += 1
        else:
            print(f'Você:{num}\nComputador:{comp} \nResultado:{num + comp}\nDeu IMPAR! NOOB, você \033[31mPerdeu\033[m')
            break
    elif escolha == 'I':
        if (num + comp) % 2 == 1:
            print(f'Você:{num}\nComputador:{comp}\nResultado:{num + comp}\nDeu Impar!! Você \033[36mGanhou\033[m')
            win += 1
        else:
            print(f'Você:{num}\nComputador:{comp} \nResultado:{num + comp}\nDeu Par! Loser, você \033[31mPerdeu\033[m')
            break
    else:
        print('É IMPAR OU PAR [P/I], ANIMAL.')
    print(20 * '=')
print(f'\n{20 * "="}\nFim de Jogo\nVocê teve {win} vitórias consecutivas.\n{20 * "="}')
