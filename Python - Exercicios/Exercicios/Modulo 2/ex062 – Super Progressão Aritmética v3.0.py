# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

pa=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=1
termos=11
salvar=0
while cont < termos:
    print(f'O termo {cont} tem a PA:{pa}')
    pa += razao
    cont+=1
    if cont==termos:
        salvar=termos
        termos=int(input('Deseja ver mais quantos termos?\nPara sair digite 0: '))
        if termos!=0:
            termos+=salvar

print('Programa finalizado com sucesso.')