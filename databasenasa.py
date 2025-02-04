import requests

# Substitua sua chave da API abaixo
API_KEY = "8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv"

# Endpoint da API do Mars Rover (exemplo de endpoint para imagens do rover Perseverance)
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/photos?sol=1000&api_key={API_KEY}"

# Função para obter dados
def obter_dados_mars_rover():
    try:
        # Enviar solicitação GET para o endpoint
        response = requests.get(url)
        
        # Verificar se a resposta foi bem-sucedida (código 200)
        if response.status_code == 200:
            dados = response.json()
            fotos = dados.get('photos', [])
            
            if fotos:
                print(f"Total de fotos encontradas: {len(fotos)}")
                for foto in fotos[:5]:  # Exibe as primeiras 5 fotos
                    print(f"Foto URL: {foto['img_src']}")
                    print(f"Sol: {foto['sol']}")
                    print(f"Data: {foto['earth_date']}")
                    print("-" * 30)
            else:
                print("Nenhuma foto encontrada para o sol especificado.")
        else:
            print("Erro na solicitação. Código de status:", response.status_code)
    
    except Exception as e:
        print("Erro ao fazer a requisição:", e)

# Chamar a função para buscar dados
obter_dados_mars_rover()
