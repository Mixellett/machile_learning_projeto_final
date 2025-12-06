import requests

def enviar_avaliacao():
    """
    Solicita uma avaliação ao usuário e envia para a API.
    """
    API_URL = "http://localhost:8000/predict"
    
    print("--- Classificador de Avaliações Amazon ---")
    avaliacao = input("Deixe sua avaliação: ")
    print("---------------------------------------")
    
    payload = {
        "text": avaliacao
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            resultado = response.json()
            predicao = resultado.get("prediction", "Erro ao obter a predição")
            if predicao == 1:
                predicao_label = "Positivo"
            elif predicao == 0:
                predicao_label = "Negativo"
            else:
                predicao_label = f"Desconhecido (código: {predicao})"
            print(f"✅ Predição da API: {predicao_label}")
        else:
            print(f"❌ Erro ao conectar com a API. Código de Status: {response.status_code}")
            print(f"Detalhes: {response.text}")

    except requests.exceptions.ConnectionError:
        print("🛑 Erro de Conexão: Certifique-se de que o contêiner Docker está rodando na porta 8000.")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")

if __name__ == "__main__":
    enviar_avaliacao()
