def leiaDinheiro(texto):
    valido = False
    while not valido:
        numero = str(input(texto)).replace(',', '.').strip()
        if numero.isalpha() or numero.strip() == '':
            print(f'\033[0;31m"{numero}" é um preço invalido.\033[m')
        else:
            return float(numero)
