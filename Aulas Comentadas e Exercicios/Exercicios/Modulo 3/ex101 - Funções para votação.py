# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def linha():
    """
    ->Cria uma linha divisória
    """
    print('-' * 30)


def voto(num):
    """
    -> Mostra a situação eleitoral da pessoa pelo ano de nascimento.
    :param num: idade da pessoa
    """
    from datetime import datetime
    idade = datetime.now().year - num
    if idade < 18:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')


# Programa Principal
linha()
voto(int(input('Em que ano você nasceu? ')))
linha()
