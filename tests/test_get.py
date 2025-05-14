import pandas as pd
from utils.data_collector import get_brt_data

def test_get_brt_data_returns_dataframe():
    df = get_brt_data()

    # Verifica se é um DataFrame
    assert isinstance(df, pd.DataFrame)

    # Verifica se não está vazio
    assert not df.empty

    # Verifica se existe a coluna 'veiculos'
    assert 'veiculos' in df.columns

    # Verifica se o primeiro item de 'veiculos' é um dicionário ou lista de dicionários
    primeiro_item = df['veiculos'].iloc[0]
    assert isinstance(primeiro_item, (dict, list))
