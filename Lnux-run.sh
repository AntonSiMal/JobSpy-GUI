#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

# Verificar que exista Python 3
if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: Python 3 no está instalado. Instálalo con tu gestor de paquetes (ej. sudo apt install python3 python3-venv)."
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual (.venv)..."
    python3 -m venv .venv
fi

# Activar entorno virtual e instalar/actualizar dependencias
source .venv/bin/activate
echo "Instalando/actualizando dependencias..."
python -m pip install --upgrade pip
pip install --upgrade python-jobspy streamlit openpyxl

# Lanzar la interfaz gráfica
echo "Iniciando interfaz de JobSpy..."
streamlit run app.py
