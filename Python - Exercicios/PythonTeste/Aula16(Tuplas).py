# AS TUPLAS SÃO IMUTÁVEIS, NÃO É POSSÍVEL TROCAR OS VALORES DE UMA TUPLA.

# print(lanche[2]) mostra o valor na posiçao 2.
# print(lanche[0:2]) mostra o valor posição 0 e 1.
# print(lanche[1:]) mostra da posição 1 até o final.
# print(lanche[-1]) mostra a ultima posiçao. Conta de forma contraria.
# print(lanche[-2:] mostra da posição -2 até o final a direita.
# len(lanche) mostra quantas posições. (Len significa comprimento)

# for c in lanche: mostra cada posição.
#   print(c)

#print(max(TUPLA)) - Mostra o maior valor.
#print(min(TUPLA)) - Mostra o maior valor.

# Utiliza () para as tuplas.
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
pos = 0

for comida in lanche:
    print(f'Eu vouuuuuu comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')  # Mostrando a posição na estrutura com FOR e IN

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  # Utilizar a posição para facilitar a visualização.

print(lanche[:2])
print(sorted(lanche))  # Coloca em ordem alfabetica ou numerica

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)  # Mostra a junção das tuplas e nao o somatório dos valores.
print(c.count(2))  # Mostra quantas vezes o numero 2 aparece.
print(c.index(8))  # Mostra em qual posição está.
print(c.index(5, 1))  # Mostra a segunda posição do numero 5.

pessoa = ('Alexandre', 24, 'M', 90.00)
cont = 0
while cont < 4:
    print(pessoa[cont])
    cont += 1
