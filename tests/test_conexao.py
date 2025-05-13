import requests

url = "https://dados.mobilidade.rio/gps/brt"
res = requests.get(url)

print("Status da requisição:", res.status_code)
