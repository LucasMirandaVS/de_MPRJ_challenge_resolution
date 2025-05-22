import pandas as pd
import os
import time
from datetime import datetime
from prefect import flow, task, get_run_logger
from utils.data_collector import get_brt_data
from utils.gcs_utils import upload_to_gcs
from dotenv import load_dotenv

load_dotenv() 

@task
def collect_minute_data():
    logger = get_run_logger()
    logger.info("Coletando dados da API do BRT...")
    return get_brt_data()

@flow(name="BRT GPS Pipeline")
def brt_pipeline():
    all_data = []

    for i in range(10):
        print(f"Captura {i+1}/10")
        df = collect_minute_data()
        all_data.append(df)
        time.sleep(60)  # espera 1 minuto

    final_df = pd.concat(all_data, ignore_index=True)
    
    file_name = f"brt_data_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"
    final_df.to_csv(file_name, index=False)

    # Substitua pelo seu bucket e caminho desejado
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    upload_to_gcs(bucket_name, file_name, f"brt_data/{file_name}")

if __name__ == "__main__":
    brt_pipeline()
