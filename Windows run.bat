@echo off
setlocal
cd /d "%~dp0"

REM Buscar Python (usa 'py -3' si está disponible, o 'python')
set "PYTHON_CMD="
where py >nul 2>nul && set "PYTHON_CMD=py -3"
if not defined PYTHON_CMD (
    where python >nul 2>nul && set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    echo Error: No se encontro Python instalado en el sistema.
    echo Descargalo desde https://www.python.org/downloads/ y marca "Add python.exe to PATH".
    pause
    exit /b 1
)

REM Crear entorno virtual si no existe
if not exist ".venv\Scripts\python.exe" (
    echo Creando entorno virtual (.venv)...
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 (
        echo Error al crear el entorno virtual.
        pause
        exit /b 1
    )
)

REM Instalar/actualizar dependencias dentro del entorno virtual
echo Instalando/actualizando dependencias...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install --upgrade python-jobspy streamlit openpyxl
if errorlevel 1 (
    echo Error al instalar las dependencias.
    pause
    exit /b 1
)

REM Lanzar la interfaz grafica
echo Iniciando interfaz de JobSpy...
.venv\Scripts\streamlit.exe run app.py

pause
