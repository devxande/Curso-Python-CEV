# Digitar varios numeros e adicionar na lista
# Caso ja exista nao sera adicionado
# exibir todos os valores unicos adicionados em ordem crescente

valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('O valor digitado já está na lista.')
    else:
        valores.append(valor)
        print('Valor digitado com sucesso.')

    # Sair
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Gostaria de adicionar mais valores? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break

valores.sort()
print(f'''\n**Exibindo resultados**
Sua lista em ordem crescente é: ''', end='')
for c in valores:
    print(f'{c}...', end='')
