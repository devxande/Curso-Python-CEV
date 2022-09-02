# Criar uma funçao voto()
# Recebe como parametro o ano de nascimento
# Retorna um valor inteiro
# Indicando tem o voto Negado -18, Obrigatorio ou opcional+65


from datetime import datetime


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
