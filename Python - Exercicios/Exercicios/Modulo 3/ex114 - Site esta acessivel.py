import requests as requests

try:
    request = requests.get('http://www.pudim.com.br/',timeout=5)
except (requests.ConnectionError, requests.Timeout) as erro:
    print(f'Não foi possível acessar o site do Pudim.\nERRO: ({erro})')
else:
    print('Conexão Verificada...\nO site do Pudim está ONLINE!')