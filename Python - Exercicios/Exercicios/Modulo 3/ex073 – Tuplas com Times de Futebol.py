# Tupla com 20 times do brasileirão.
# Mostrar 5 primeiros colocados.
# 4 ultimos.
# Times em ordem alfabética.
# Posição do São Paulo.

times = ('Atlético-MG','Flamengo','Palmeiras',
         'Fortaleza','Corinthians',
         'Bragantino','Fluminense','América-MG',
         'Atlético-GO','Santos', 'Ceará',
         'Inter', 'São Paulo', 'Atletico-PR',
         'Cuiabá', 'Juventudade', 'Grêmio',
         'Bahia', 'Sport','Chapecoense')
c=0
for c in range(c,5):
    print(times[c],end=',') if c!=4 else print(times[c],end='\n')
print(times.sorted())
print(f'{50*"*"}\nOs ultimos 4 times são: {times[-4:]}')
print(f'\n{"*"*50}\nTimes em ordem alfabética: {sorted(times)}')
print(f'\n{"*"*50}\nO São Paulo está na posição {times.index("São Paulo")} da tabela.')
