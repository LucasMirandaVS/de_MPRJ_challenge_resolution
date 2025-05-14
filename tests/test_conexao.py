import requests

def test_status_code_brt_api():
    url = "https://dados.mobilidade.rio/gps/brt"
    res = requests.get(url)
    assert res.status_code == 200
