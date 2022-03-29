# Exercício Python 040: Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'REPROVADO! Estude mais, sua média foi apenas {media}.')
elif 5.0 <= media <= 6.9:
    print(f'Você está de recuperação com a média {media}, foi quase!')
else:
    print(f'Você foi aprovado com a média {media}, parabéns!')
