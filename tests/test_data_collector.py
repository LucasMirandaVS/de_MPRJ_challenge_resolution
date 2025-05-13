from utils.data_collector import get_brt_data
import pandas as pd

def test_brt_data_format(monkeypatch):
    # Simula resposta da API
    mock_response = [{"id": 1, "lat": -22.9, "lon": -43.2}]
    
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self): return mock_response
            status_code = 200
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    df = get_brt_data()
    
    assert isinstance(df, pd.DataFrame)
    assert "coleta_ts" in df.columns
    assert df.loc[0, "id"] == 1
