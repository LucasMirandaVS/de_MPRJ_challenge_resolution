import os
from dotenv import load_dotenv

load_dotenv()

# Diretórios base
DATA_DIR = "data"
LOG_DIR = "logs"

# Nome do bucket no GCS
GCS_BUCKET = os.getenv("GCS_BUCKET_NAME", "bucket_default")

# API do BRT
BRT_API_URL = "https://dados.mobilidade.rio/gps/brt"
