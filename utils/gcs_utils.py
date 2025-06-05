import os
from google.cloud import storage
from utils.logger import logger

def upload_to_gcs(bucket_name, local_file_path, destination_blob_name):
    if not os.path.exists(local_file_path):
        logger.error(f"Arquivo {local_file_path} não encontrado.")
        raise FileNotFoundError(f"{local_file_path} não existe.")

    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)
        logger.info(f"Upload concluído: gs://{bucket_name}/{destination_blob_name}")
    except Exception as e:
        logger.error(f"Falha no upload para GCS: {e}")
        raise
