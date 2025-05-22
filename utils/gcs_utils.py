from google.cloud import storage

def upload_to_gcs(bucket_name, local_file_path, destination_blob_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)
        print(f"Upload concluído: gs://{bucket_name}/{destination_blob_name}")
    except Exception as e:
        print(f"[ERRO] Falha no upload: {e}")
        raise
