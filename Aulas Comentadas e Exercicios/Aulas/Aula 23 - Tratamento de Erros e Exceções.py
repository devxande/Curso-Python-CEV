# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
# Aprenda como usar a estrutura try except no Python de uma forma simples.
oper = False
# Operação
while oper is not True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b

    # Cada bloco de erro pode ter sua resposta.
    except (ValueError, TypeError) as erro:
        print(f'''Tivemos um erro com os tipos de dados que voce digitou.
    Erro encontrado foi {erro.__class__}.''')
    except KeyboardInterrupt as erro:
        print(f'''O usuário digitou nenhum valor.
    Erro encontrado foi {erro.__class__}.''')
    except ZeroDivisionError as erro:
        print(f'''Não é possível dividir um número por zero.
    Erro encontrado foi {erro.__class__}.''')
    # Falhou, resposta padrão/genérico Exception;
    except Exception as erro:
        print(f'Erro encontrado foi {erro.__cause__}.')

    # Deu certo
    else:
        print(f'O resultado é {r:.1f}')
        oper = True

    # Certo/Falha
    finally:
        print('Volte sempre! Obrigado.')
