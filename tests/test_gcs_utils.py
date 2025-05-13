from utils.gcs_utils import upload_to_gcs
from unittest.mock import MagicMock, patch

@patch("utils.gcs_utils.storage.Client")
def test_upload_to_gcs(mock_client_class):
    mock_client = MagicMock()
    mock_bucket = MagicMock()
    mock_blob = MagicMock()

    mock_client.bucket.return_value = mock_bucket
    mock_bucket.blob.return_value = mock_blob
    mock_client_class.return_value = mock_client

    # Chama a função
    upload_to_gcs("bucket-teste", "arquivo.csv", "pasta/arquivo.csv")

    # Verificações
    mock_bucket.blob.assert_called_once_with("pasta/arquivo.csv")
    mock_blob.upload_from_filename.assert_called_once_with("arquivo.csv")
