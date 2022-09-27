# Ler valor 0 a 20 e verificar.
# Mostrar o valor por extenso.
num = 0
erro = ' '
contagem = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five',
            'Six', 'Seven', 'Eight', 'Nine', 'Ten'
            , 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while erro not in 'S':
    num = int(input('Digite um valor entre 0 a 20: '))
    if 0 <= num <= 20:
        erro = 'S'
print(f'O numero {num} por extenso é: {contagem[num]}')
