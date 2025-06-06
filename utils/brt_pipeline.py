import pandas as pd
import os
import time
from datetime import datetime
from prefect import flow, task, get_run_logger
from utils.data_collector import get_brt_data
from utils.gcs_utils import upload_to_gcs
from config.settings import DATA_DIR, GCS_BUCKET
from utils.logger import logger
from dotenv import load_dotenv

load_dotenv()

@task
def collect_minute_data():
    logger = get_run_logger()
    logger.info("Coletando dados da API do BRT...")
    return get_brt_data()

@flow(name="BRT GPS Pipeline")
def brt_pipeline(duration_min: int = 10):
    logger = get_run_logger()
    all_data = []

    for i in range(duration_min):
        logger.info(f"Captura {i+1}/{duration_min}")
        df = collect_minute_data()
        all_data.append(df)
        time.sleep(60)

    final_df = pd.concat(all_data, ignore_index=True)

    # Garantir que a coluna coleta_ts exista
    if 'coleta_ts' not in final_df.columns:
        logger.error("Coluna 'coleta_ts' não encontrada. Abortando salvamento.")
        return

    # Particionar por data
    final_df['coleta_data'] = pd.to_datetime(final_df['coleta_ts']).dt.date
    os.makedirs(DATA_DIR, exist_ok=True)

    for data_coleta in final_df['coleta_data'].unique():
        df_particao = final_df[final_df['coleta_data'] == data_coleta].copy()
        file_name = f"brt_data_{data_coleta}_{datetime.utcnow().strftime('%H%M%S')}.csv"
        file_path = os.path.join(DATA_DIR, file_name)
        df_particao.drop(columns=['coleta_data'], inplace=True)
        df_particao.to_csv(file_path, index=False)

        destino_gcs = f"brt_data/{data_coleta}/{file_name}"
        upload_to_gcs(GCS_BUCKET, file_path, destino_gcs)
