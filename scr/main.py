import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import get_dataset_url
import pandas as pd

# Carga el dataset RAW
url_raw = get_dataset_url("A Systematic Review of Approaches Metrics and Challenges.xlsx")
print("Descargando dataset RAW desde:", url_raw)
df = pd.read_csv(url_raw)
print(df.head())

# Carga un dataset procesado (opcional)
url_processed = get_dataset_url("A Systematic Review of Approaches Metrics and Challenges_clean.xlsx", processed=True)
print("Dataset procesado:", url_processed)
