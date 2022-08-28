# criar funçao maior()
# Recebe varios parametros inteiros
# mostrar qual deles é o maior.
def lin():
    print(f'-=-' * 20)


def maior(lst):
    lin()
    print('Analisando os valores passados...')
    pos = 0
    while pos < len(lst):
        print(f'{lst[pos]}', end=' ')
        pos += 1
    print(f'Foram informados {len(lst)} ao todo.')
    print(f'O maior valor informado foi o {max(lst)}')


# PROGRAMA PRINCIPAL
lista = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    # SAIR
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar novo número? [S/N]')).upper()[0]
        if sair not in 'SN':
            print('Opção invalida!')
    if sair == 'N':
        break
maior(lista)
