# Exercício Python 109: Modifique as funções que form criadas no desafio 107
# para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, False)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num,10, False)}')
print(f'Dimiundo 13%, temos R${moeda.diminuir(num,13)}')
