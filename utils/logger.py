import logging
import os
from config.settings import LOG_DIR

# Garante que o diretório de logs exista
os.makedirs(LOG_DIR, exist_ok=True)

# Define o caminho do arquivo de log
LOG_FILE = os.path.join(LOG_DIR, "pipeline.log")

# Configuração básica do logger
logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",  # 'a' para append, 'w' para sobrescrever
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Instância global de logger
logger = logging.getLogger("brt_logger")
