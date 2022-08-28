# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
time = []
gols = []
jogadorGols = []

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['total'] = 0
    for cont in range(0, jogador['partidas']):
        gols.append(int(input(f'  Quantos gols na partida {cont + 1}? ')))
        jogador['total'] += gols[cont]
    jogadorGols.append(gols[:])
    gols.clear()
    time.append(jogador.copy())

    # SAIR
    sair = ' '
    if sair not in 'SN':
        sair = str(input('Adicionar novo jogador? [S/N]')).upper()[0]
    if sair == 'N':
        break

print(f'''\n{"-=-" * 20}
 cod    nome            gols     total''')
for cont in range(0, len(time)):
    print(f'{cont:>4}   {time[cont]["nome"]:<15}  {jogadorGols[cont]}   {time[cont]["total"]}')
print(f'{"-=-" * 20}')

while sair != 999:
    # sair
    sair = int(input('\nMostrar dados de qual jogador? (999 para Fechar) '))
    if sair == 999:
        break
    print(f'--- LEVANTAMENTO DO JOGADOR {time[sair]["nome"]} ---')
    for cont in range(0, time[sair]['partidas']):
        print(f'No jogo {cont + 1} fez {jogadorGols[sair][cont]} gols.')
