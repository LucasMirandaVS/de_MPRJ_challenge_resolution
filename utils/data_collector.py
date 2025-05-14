import requests
import pandas as pd
from datetime import datetime

def get_brt_data():
    url = "https://dados.mobilidade.rio/gps/brt"  
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code}")

    data = response.json()
    df = pd.DataFrame(data)

    # Adiciona timestamp de coleta
    df['coleta_ts'] = datetime.utcnow()

    return df
