import requests
import json

# Substitua pela sua chave de API pessoal
api_key = '8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv'  # Use sua chave obtida no portal da NASA

# Defina a data de início e fim
start_date = '2023-02-01'
end_date = '2023-02-02'

# URL da API com os parâmetros de consulta
url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'

# Fazer a requisição GET
response = requests.get(url)

# Se a requisição for bem-sucedida
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))  # Exibe os dados formatados em JSON
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")
