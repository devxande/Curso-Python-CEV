nome = str(input('Qual seu nome?').lower())
if nome == 'alexandre':
    print('Que nome bonito!')
elif nome=='pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é popular')
elif nome in 'ana carolina vitoria claudia':
    print('Belo nome feminino')
else:
    print('Seu nome é normal.')
print(f'Tenha um bom dia, {nome}!')