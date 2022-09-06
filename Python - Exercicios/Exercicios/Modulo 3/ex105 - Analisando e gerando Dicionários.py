# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = {
        'total': len(num),
        'maior': 0,
        'menor': 10,
        'media': 0,
    }
    media = 0
    for v in num:
        # Maior
        if turma['maior'] < v:
            turma['maior'] = v
        # Menor
        if turma['menor'] > v:
            turma['menor'] = v
        # Media
        media += v
    turma['media'] = media / len(num)
    if sit == True:
        if turma['media'] >= 7:
            turma['situação'] = 'Boa!'
        elif turma['media'] >= 4:
            turma['situação'] = 'Razoável!'
        elif turma['media'] < 4:
            turma['situação'] = 'Ruim!'
    return turma


# Código Principal
resp = notas(9, 9, 5.5, 10, sit=True)
print(resp)
help(notas)
