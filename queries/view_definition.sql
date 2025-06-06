CREATE OR REPLACE VIEW `projeto-estudando-gcp.brtdata.brt_view_completa` AS
SELECT
  JSON_EXTRACT_SCALAR(veiculos, '$.codigo') AS codigo,
  JSON_EXTRACT_SCALAR(veiculos, '$.linha') AS linha,
  SAFE_CAST(JSON_EXTRACT_SCALAR(veiculos, '$.latitude') AS FLOAT64) AS latitude,
  SAFE_CAST(JSON_EXTRACT_SCALAR(veiculos, '$.longitude') AS FLOAT64) AS longitude,
  SAFE_CAST(JSON_EXTRACT_SCALAR(veiculos, '$.velocidade') AS FLOAT64) AS velocidade,
  PARSE_TIMESTAMP('%s', CAST(CAST(JSON_EXTRACT_SCALAR(veiculos, '$.dataHora') AS INT64) / 1000 AS STRING)) AS dataHora,
  coleta_ts
FROM `projeto-estudando-gcp.brtdata.brt_unificado`

UNION ALL

SELECT
  JSON_EXTRACT_SCALAR(veiculos, '$.codigo') AS codigo,
  JSON_EXTRACT_SCALAR(veiculos, '$.linha') AS linha,
  SAFE_CAST(JSON_EXTRACT_SCALAR(veiculos, '$.latitude') AS FLOAT64) AS latitude,
  SAFE_CAST(JSON_EXTRACT_SCALAR(veiculos, '$.longitude') AS FLOAT64) AS longitude,
  SAFE_CAST(JSON_EXTRACT_SCALAR(veiculos, '$.velocidade') AS FLOAT64) AS velocidade,
  PARSE_TIMESTAMP('%s', CAST(CAST(JSON_EXTRACT_SCALAR(veiculos, '$.dataHora') AS INT64) / 1000 AS STRING)) AS dataHora,
  coleta_ts
FROM `projeto-estudando-gcp.brtdata.unificado_2`;
