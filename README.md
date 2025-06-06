# Pipeline de Coleta de Dados do BRT - RJ

Projeto desenvolvido com o objetivo de construir um pipeline automatizado para capturar, armazenar e analisar dados do transporte público do BRT-RJ.



## Objetivo

- Capturar dados minuto a minuto da frota de ônibus do BRT-RJ via API pública.
- Armazenar os dados em arquivos `.csv` no Google Cloud Storage (GCS).
- Tornar os dados acessíveis e prontos para análise no BigQuery.
- Criar uma view unificada com todos os dados coletados.



## Arquitetura

```mermaid
graph TD;
    API_BRT["API do BRT-RJ"]
    Prefect["Prefect (orquestrador)"]
    CSV["Arquivos CSV"]
    GCS["Google Cloud Storage"]
    BQ_Tabela["BigQuery - Tabelas Externas"]
    BQ_View["BigQuery - View Unificada"]

    API_BRT --> Prefect
    Prefect --> CSV
    CSV --> GCS
    GCS --> BQ_Tabela
    BQ_Tabela --> BQ_View



## Tecnologias Utilizadas
- Python 3.12
- Prefect (orquestração local com Docker Agent)
- Google Cloud Storage (GCS)
- Google BigQuery
- Bibliotecas: pandas, requests, dotenv, google-cloud-storage



##  Etapas do Pipeline
- Captura de dados minuto a minuto da API do BRT.
- Criação de CSVs com os dados coletados (particionados por data).
- Upload automático para o GCS.

## Melhorias Futuras
- Executar o pipeline 100% na nuvem (ex: Cloud Run + Prefect Cloud).
- Agendamento com Cloud Scheduler + Pub/Sub.
- Parsing completo dos dados aninhados.
- Dashboard no Looker Studio.