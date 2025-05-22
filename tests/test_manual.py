from google.cloud import storage

client = storage.Client()
bucket = client.bucket("biucket_brt")
blob = bucket.blob("brt_data/teste.txt")
blob.upload_from_string("Upload funcionando!")
