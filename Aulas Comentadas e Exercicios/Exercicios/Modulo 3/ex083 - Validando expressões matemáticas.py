# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

esquerda = direita = 0
expressao = str
valores = []

expressao = (str(input('Digite sua expressão matématica: ')))

# Usando list()
valores = list(expressao)

esquerda = valores.count('(')
direita = valores.count(')')
if esquerda != direita:
    print('A expressão está INCORRETA!')
else:
    print('A expressão está CORRETA!')

# Usando for
for num in expressao:
    valores.append(num)
if esquerda != direita:
    print('A expressão está INCORRETA!')
else:
    print('A expressão está CORRETA!')
