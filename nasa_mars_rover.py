import requests
import webbrowser

# Configurações da API
API_KEY = "8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv"  # Substitua com sua chave API da NASA
URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"  # URL para as fotos do Mars Rover

# Parâmetros da requisição
params = {
    "earth_date": "2023-01-01",  # Substitua pela data desejada (formato: AAAA-MM-DD)
    "api_key": API_KEY
}

try:
    # Faz a requisição para a API
    response = requests.get(URL, params=params)
    response.raise_for_status()  # Levanta um erro se a requisição falhar

    # Processa os dados da resposta
    data = response.json()  # Converte o JSON para um dicionário
    photos = data.get("photos", [])  # Acessa a lista de fotos

    if photos:
        print(f"Encontradas {len(photos)} fotos.")
        for photo in photos[:5]:  # Exibe até 5 fotos
            print(f"Foto tirada por {photo['camera']['full_name']} na data {photo['earth_date']}: {photo['img_src']}")
            # Abre a foto no navegador
            webbrowser.open(photo['img_src'])
    else:
        print("Nenhuma foto disponível para essa data.")

except requests.RequestException as e:
    print(f"Erro ao buscar dados: {e}")
