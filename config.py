"""
config.py — Configuración general del proyecto.
Autor: Marco Robles
Descripción:
Define rutas dinámicas para datasets alojados en GitHub (raw y processed).
Permite cargar datos directamente desde HTTPS sin depender del entorno local.
"""

import sys

# === Nombre del proyecto ===
PROJECT_NAME = "revista-cientifica-1"

# === Bases en GitHub (rutas públicas) ===
RAW_BASE = "https://raw.githubusercontent.com/iainvestigacionmrobles/revista-cientifica-1/main/dataset/raw/"
PROCESSED_BASE = "https://raw.githubusercontent.com/iainvestigacionmrobles/revista-cientifica-1/main/dataset/processed/"

# === Detección automática de entorno ===
def get_runtime_environment() -> str:
    """Detecta el entorno de ejecución."""
    if "google.colab" in sys.modules:
        return "colab"
    elif "ipykernel" in sys.modules:
        return "vscode/jupyter"
    else:
        return "local"

# === Función para construir URL completa ===
def get_dataset_url(filename: str, processed: bool = False) -> str:
    """
    Retorna la URL completa de un dataset alojado en GitHub.
    - filename: nombre del archivo (ej. 'veteran.csv')
    - processed: si es True, busca en 'processed', de lo contrario en 'raw'
    """
    base = PROCESSED_BASE if processed else RAW_BASE
    return base + filename

# === Función para mostrar resumen ===
def show_config_info():
    """Muestra la configuración actual y entorno."""
    print("📦 Proyecto:", PROJECT_NAME)
    print("🌐 Entorno:", get_runtime_environment())
    print("🔗 RAW_BASE:", RAW_BASE)
    print("🔗 PROCESSED_BASE:", PROCESSED_BASE)

# === Ejemplo de uso directo ===
if __name__ == "__main__":
    show_config_info()
    print("🧠 Ejemplo URL RAW:", get_dataset_url("veteran.csv"))
    print("🧠 Ejemplo URL PROCESSED:", get_dataset_url("veteran_clean.csv", processed=True))
