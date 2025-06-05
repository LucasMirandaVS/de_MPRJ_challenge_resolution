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

    file_name = f"brt_data_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"
    os.makedirs(DATA_DIR, exist_ok=True)
    file_path = os.path.join(DATA_DIR, file_name)
    final_df.to_csv(file_path, index=False)

    upload_to_gcs(GCS_BUCKET, file_path, f"brt_data/{file_name}")
