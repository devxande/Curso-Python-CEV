# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
cores = {
    'red': '\033[1;31m',
    'amarelo': '\033[0;33m',
    'green': '\033[0;32m',
    'clear': '\033[0m'
}

print('-=-' * 20, '\n{}**Preencher as informações abaixo**{}'.format(cores['amarelo'], cores['clear']))
casa = float(input('Qual o valor da casa desejada: R$'))
salario = float(input('Qual o salário mensal do comprador: R$'))
anos = float(input('Quantos anos para pagar: '))

print('-=-' * 20, '\n{}Processando..{}\n'.format(cores['red'], cores['clear']), '-=-' * 20)
sleep(2)

prestacao = casa / (anos * 12)

if prestacao <= salario * 0.3:
    print('{}Emprestimo APROVADO!{}\n'.format(cores['green'], cores['clear']),
          'Valor da casa: R${:.2f}\n'.format(casa),
          'Valor da prestação é de R${:.2f}\n'.format(prestacao),
          'Quantidade de meses: {:.0f}'.format(anos * 12))
else:
    print('{}EMPRESTIMO NEGADO!{}\n'
          'O salário do comprador é incompativél com o valor da casa'.format(cores['red'], cores['clear']))
