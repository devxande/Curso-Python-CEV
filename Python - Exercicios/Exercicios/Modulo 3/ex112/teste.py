# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui.

from utilidadescev import dados
from utilidadescev import moeda

num = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(num, 10, 15)
