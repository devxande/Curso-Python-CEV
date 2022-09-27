# Exercício Python 114: Crie um código em Python que teste
# se o site pudim está acessível pelo computador usado.

import requests as requests
import urllib.request

try:
    request = requests.get('http://www.bolsonaro.com.br//', timeout=5)
except (requests.ConnectionError, requests.Timeout) as erro:
    print(f'Não foi possível acessar o site do Pudim.\nERRO: ({erro})')
else:
    print('Conexão Verificada...\nO site do Pudim está ONLINE!')

# Segunda forma de validar URL.
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Deu erro!')
else:
    print('Tudo OK!')
