import requests
import pandas as pd
from datetime import datetime, timezone
from utils.logger import logger
from config.settings import BRT_API_URL
from requests.exceptions import RequestException

def get_brt_data():
    try:
        response = requests.get(BRT_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data:
            logger.warning("API retornou uma resposta vazia.")
            return pd.DataFrame()

        df = pd.DataFrame(data)
        df['coleta_ts'] = datetime.now(timezone.utc)
        return df

    except RequestException as e:
        logger.error(f"Erro ao acessar a API do BRT: {e}")
        raise

    except ValueError as e:
        logger.error(f"Erro ao converter JSON: {e}")
        raise
