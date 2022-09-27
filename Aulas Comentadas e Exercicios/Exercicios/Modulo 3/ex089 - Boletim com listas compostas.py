# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

listaTotal = []
dados = []

while True:
    dados.append(str(input('Digite o nome: ').upper()))
    dados.append(float(input('Digite a primeira nota: ')))
    dados.append(float(input('Digite a segunda nota: ')))
    listaTotal.append(dados[:])
    dados.clear()

    # Sair
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Adicionar novo aluno? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break

print(f'''{10 * "-=-"}
No. NOME           MEDIA
{10 * "---"}''')

pos = media = 0
for num in listaTotal:
    while True:
        media = (listaTotal[pos][1] + listaTotal[pos][2]) / 2
        print(f'''{pos}   {listaTotal[pos][0]:<10}     {media:^3}''')
        pos += 1
        break

print()
aluno = 0
while True:
    aluno = int(input('\nMostrar notas de qual aluno?  (999 Interrompe): '))
    if aluno == 999:
        print('Programa encerrado!')
        break
    if aluno <= len(listaTotal) - 1:
        print(f'''\n{"*" * 5 + "  NOTAS  " + "*" * 5}
NOME: {listaTotal[aluno][0]} / NOTAS: {listaTotal[aluno][1]} / {listaTotal[aluno][2]}''')
    if aluno > len(listaTotal) - 1:
        print('Opcao invalida!')
