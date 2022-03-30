#Tupla unica com produtose valores na sequencia.
# mostrar listagem de preços tabulada.

produtos = ('Memoria Ram', 200,
            'Processador', 850.00,
            'SSD',  100.00,
            'Placa mãe', 530.00,
            'Air cooler', 120.00,
            'Fonte', 470.00,
            'Gabinete', 330,
            'Fans', 150.00,
            'Inooth', 1000.00
            )
print(F'''{40*"-"}
{"LISTAGEM DE PREÇOS":^40}
{40*"-"}''')
# for c in range(0,(len(produtos)),2):
#     print(f'{produtos[c]:.<20}{produtos[c+1]:.>10.2f}')
# print(30*"-")

# Resolução
for pos in range(0,len(produtos)):
    if pos % 2 ==0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print(40*"-")