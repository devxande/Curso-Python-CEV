# 1- Estilo(0=none 1=negrito 4=sublinhada 7=inverte texto e fundo.)
# 2- Texto
# 3- Fundo
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m
# \033[7;30m
print('\033[7;30;44mOlá mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\33[m e \33[31m{b}\33[m')

nome = 'Alexandre'
print(f'Olá, muito prazer em te conhecer, \033[4;34m{nome}\33[m')

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7,30m'}
print('Era uma {}vez{} a {}carochinha{}'.format(cores['azul'], cores['limpa'], cores['amarelo'], cores['limpa']))
