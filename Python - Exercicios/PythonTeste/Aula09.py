'''print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('boba'))
print('Curso' in frase)
print(frase.replace('Python','android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())'''

# Tira os espaços laterais
frase1 = '  Aprenda Python '
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())

frase = '12 34 video 89'
# Divide em uma lista
print(frase.split())
# Adiciona entre as letras
print('-'.join(frase))

print(len(frase.strip()))
print(frase.lower().find('video'))

dividido = frase.split()
print(dividido[2])
print(dividido[2][3])
