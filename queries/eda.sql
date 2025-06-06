# Contagem total de registros
SELECT COUNT(*) AS total_registros
FROM `projeto-estudando-gcp.brtdata.brt_view_completa`;

# Distribuição de coletas por data
SELECT
  DATE(coleta_ts) AS data_coleta,
  COUNT(*) AS total
FROM `projeto-estudando-gcp.brtdata.brt_view_completa`
GROUP BY data_coleta
ORDER BY data_coleta DESC;

# Top 10 linhas mais registradas
SELECT
  linha,
  COUNT(*) AS total
FROM `projeto-estudando-gcp.brtdata.brt_view_completa`
GROUP BY linha
ORDER BY total DESC
LIMIT 10;

# Velocidade média por linha
SELECT
  linha,
  ROUND(AVG(velocidade), 2) AS velocidade_media,
  COUNT(*) AS registros
FROM `projeto-estudando-gcp.brtdata.brt_view_completa`
GROUP BY linha
ORDER BY velocidade_media DESC
LIMIT 10;

# Latitude e longitude extremas (limites geográficos)
SELECT
  MIN(latitude) AS min_latitude,
  MAX(latitude) AS max_latitude,
  MIN(longitude) AS min_longitude,
  MAX(longitude) AS max_longitude
FROM `projeto-estudando-gcp.brtdata.brt_view_completa`;

# Distribuição horária das coletas
SELECT
  EXTRACT(HOUR FROM coleta_ts) AS hora,
  COUNT(*) AS total
FROM `projeto-estudando-gcp.brtdata.brt_view_completa`
GROUP BY hora
ORDER BY hora;
