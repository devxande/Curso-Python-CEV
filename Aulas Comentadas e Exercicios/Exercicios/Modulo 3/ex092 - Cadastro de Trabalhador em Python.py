# Exercício Python 092: crie um programa que leia nome, ano de nascimento e carteira de trabalho
# cadastre-o (com idade) num dicionário.
# Se por acaso a CTPS diferir de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = {
    'nome': str(input('Nome: ')),
    'idade': datetime.now().year - int(input('Ano de nascimento: ')),
    'ctps': str(input('Carteira de Trabalho (0 não tem): '))
}

if pessoa['ctps'] != '0':
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salario: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (datetime.now().year - pessoa['contratacao']))
    print(pessoa)
    print(f'''{"*" * 5} INFORMAÇÕES {"*" * 5}
1- Nome tem o valor: {pessoa['nome']}
2- Idade tem o valor: {pessoa['idade']}
3- CTPS tem o valor: {pessoa['ctps']}
4- Contrataçao tem o valor: {pessoa['contratacao']}
5- Salario tem o valor: {pessoa['salario']}
6- Aposentadoria tem o valor: {pessoa['aposentadoria']}
{"*" * 20}''')
else:
    print(pessoa)
    print(f'''{"*" * 5} INFORMAÇÕES {"*" * 5}
1- Nome tem o valor: {pessoa['nome']}
2- Idade tem o valor: {pessoa['idade']}
3- CTPS tem o valor: {pessoa['ctps']}
{"*" * 20}''')
