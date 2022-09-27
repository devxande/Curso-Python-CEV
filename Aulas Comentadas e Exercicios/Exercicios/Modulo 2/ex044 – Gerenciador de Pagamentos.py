# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

from time import sleep

cores = {
    'title': '\033[1;30;42m',
    'branco': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'limpa': '\033[m'
}

preco = float(input('-=-' * 13
                    + '\n  **Loja do {}Gostosão Kxamp {}Estrela{}!**\n'
                    .format('\33[1m', cores['yellow'], cores['limpa'])
                    + '-=-' * 13
                    + '\n\nInforme o valor do produto:\n'
                    + '{}DIGITE AQUI:{} '.format('\033[31m', cores['limpa'])))

condicao = int(input('''\n{}Escolha uma das formas de pagamento abaixo:{}
1- Á vista Dinheiro/Cheque (10% DESC)
2- Á vista Cartão (5% DESC)
3- 2x Cartão (Sem DESC)
4- 3x ou mais Cartão (20% JUROS)
DIGITE AQUI: '''.format('\033[1m', cores['limpa'])))

print('\n', '-=-' * 10, '\n        Processando...\n', '-=-' * 10), sleep(2)

if 0 < condicao <= 4:
    print('{}**OPÇÃO VALIDA**{}'.format(cores['yellow'], cores['limpa']))
    if condicao == 1:
        print('1- Á vista Dinheiro/Cheque (10% DESC)'
              '\nValor do Produto: R$\033[32m{:.2f}\033[m'
              '\nValor total com Desconto: R$\033[32;1m{:.2f}\033[m'.format(preco, preco - (preco * 0.10)))

    elif condicao == 2:
        print('2- Á vista Cartão (5% DESC)'
              '\nValor do Produto: R$\033[32m{:.2f}\033[m'
              '\nValor total com Desconto: R$\033[32;1m{:.2f}\033[1m'.format(preco, preco - (preco * 0.05)))

    elif condicao == 3:
        print('3- 2x Cartão (Sem DESC)'
              '\nValor do Produto: R$\033[32m{:.2f}\033[m'
              '\nForma de pagamento sem descontos.'.format(preco))
    # condicao == 4
    else:
        print('4- 3x ou mais Cartão (20% JUROS)'
              '\nValor do Produto: R$\033[32m{:.2f}\033[m'
              '\nValor total com Juros: R$\033[32m{:.2f}\033[m'.format(preco, preco + (preco * 0.20)))
# condicao invalida
else:
    print('{}**OPÇÃO INVALIDA**{}\n\n{}PROGRAMA ENCERRANDO..'.format(cores['red'], cores['limpa'], '\033[1m')),sleep(2)

print('\n{}**PAGUE NO CAIXA**{}\n{}PROGRAMA ENCERRANDO..'.format(cores['blue'], cores['limpa'], '\033[1m')),sleep(2)
