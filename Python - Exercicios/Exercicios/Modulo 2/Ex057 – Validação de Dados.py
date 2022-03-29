# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Qual o seu sexo?\n[ M ] - Masculino\n[ F ] - Feminino\nOpção entre M ou F: ')).upper().strip()[0]
sair = 'n'
while sair != 's':
    if sexo == 'M':
        print('Informação correta, o sexo é Masculino.')
        sair = 's'
    elif sexo == 'F':
        print('Informação correta, o sexo é Feminino.')
        sair = 's'
    else:
        sexo = str(input('Opção invalida, digite novamente: ')).upper()
