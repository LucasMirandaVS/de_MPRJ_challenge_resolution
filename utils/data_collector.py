import requests
import pandas as pd
from datetime import datetime, timezone

def get_brt_data():
    url = "https://dados.mobilidade.rio/gps/brt"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Erro ao acessar {url} - Código: {response.status_code}")

    data = response.json()

    if not data:
        raise ValueError("A resposta da API está vazia ou malformada.")

    df = pd.DataFrame(data)
    df['coleta_ts'] = datetime.now(timezone.utc)

    return df
