# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
jogador['total'] = 0
for cont in range(0, jogador['partida']):
    gols.append(int(input(f'Quantos gols na partida {cont + 1}: ')))
    jogador['total'] += gols[cont]
jogador['gols'] = gols

# Lista
print(f'''\n{"-=-" * 20} 
{jogador}
{"-=-" * 20}''')

for k, v in jogador.items():
    print(f'''O campo {k} tem o valor {v}.''')

print(f'''{"-=-" * 20} 
Jogador {jogador['nome']} jogou {jogador['partida']} partidas.''')
for cont in range(0, jogador['partida']):
    print(f'=>Na partida {cont + 1}, fez {jogador["gols"][cont]} gols.')
print(f'Total de Gols: {jogador["total"]}')
