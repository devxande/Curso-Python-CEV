'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--fim--')
print('carro novo' if tempo <=3 else 'Carro velho')'''

n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
m = (n1 + n2)/2
print('Sua nota média foi {:.1f}'.format(m))
print('Sua média foi boa!' if m >=6 else 'Sua média foi ruim.')
if m >= 6:
    print('Sua média foi boa.')
else:
    print('Sua média foi ruim')


