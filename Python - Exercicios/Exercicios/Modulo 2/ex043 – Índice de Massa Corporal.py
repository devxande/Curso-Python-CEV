# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

from time import sleep

cores = {
    'azul': '\033[34m',
    'vermelho': '\033[31m',
    'amarelho': '\033[33m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'limpa': '\033[m'
}

altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite o seu peso (Kg): '))

print('-=-' * 10, '\nProcessando...\n', '-=-' * 10)
sleep(1)

imc = peso / (altura ** 2)
if 0 <= imc <= 100:
    if imc < 18.5:
        print('''Seu IMC é {:.2f}.
Vai comer minha filha, {}ta muito abatida!{}
{}Abaixo do peso.'''.format(imc, '\033[4m', '\033[m', cores['vermelho']))
    elif 18.5 <= imc < 25:
        print('Seu IMC é {:.2f}.\nTa no pesinho, {}fala dele!{}\n{}Peso ideal.'.format(imc, '\033[4m', '\033[m',
                                                                                       cores['amarelho']))
    elif 25 <= imc < 30:
        print('Está Sobrepeso')
    elif 30 <= imc < 40:
        print('Está Obesidade')
    elif 40 <= imc:
        print('Cuidado! Obesidade Mórbida')
else:
    print('Informações incorretas.')
