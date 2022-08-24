# Exercício Python 090. Faça um programa que leia nome e média de um aluno,
# guardando também a situação num dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {'nome': str(input('Nome: ')), 'media': float(input('Média: '))}
if aluno['media'] >= 5:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('-=-'*20)
print(f'''Nome é igual a {aluno["nome"]}.
Média é igual a {aluno["media"]}.
Situação é igual a {aluno["situacao"]}.''')

# Outra forma
print('-=-'*20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
