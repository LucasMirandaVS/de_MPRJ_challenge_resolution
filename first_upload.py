from utils.data_collector import get_brt_data
from utils.gcs_utils import upload_to_gcs
from datetime import datetime

# Gera nome do arquivo com timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
file_name = f"brt_data_{timestamp}.csv"

# Coleta os dados e salva localmente como CSV
df = get_brt_data()
df.to_csv(file_name, index=False)

# Envia o CSV para o bucket no GCS
upload_to_gcs(
    bucket_name="biucket_brt",
    local_file_path=file_name,
    destination_blob_name=file_name
)

print(f"Arquivo {file_name} salvo localmente e enviado para o bucket com sucesso!")
