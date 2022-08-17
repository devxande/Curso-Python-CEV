# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

valores = []
valor = primeiroValor = 0
for cont in range(0, 4):
    if cont == 0:
        valores.append(int(input('Digite um valor: ')))
        print('Valor adicionado final da lista.')
        primeiroValor = valores[cont]
    else:
        valor = int(input('Digite um valor: '))
        if valor >= primeiroValor:
            valores.append(valor)
            print('Valor adicionado final da lista.')
            primeiroValor = valor
        else:
            for contador in range(0, 4):
                if valor < valores[contador]:
                    valores.insert(contador, valor)
                    print(f'Valor adicionado na posição {contador} da lista.')
                    break

print(f'\n****************\nOs valores da lista em ordem foram: {valores}')
