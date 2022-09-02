# Criar uma funçao notas()
# Recebe varias notas
# Retornar as informações:
# Quantidade de notas; len()
# A maior; A menor; A média;
# e situação 7=boa


def notas(*num, sit=False):
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
resp = notas(2, 2, 5.5, 5, sit=False)
print(resp)
