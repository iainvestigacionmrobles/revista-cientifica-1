@echo off
:: ===================================================
:: Script para iniciar el entorno de trabajo local
:: Proyecto: revista-cientifica-1
:: Autor: Marco Robles
:: ===================================================

echo 🔧 Iniciando entorno virtual de Python...
cd /d D:\github\revista-cientifica-1

:: Activa el entorno virtual
call venv\Scripts\activate.bat

:: Muestra confirmación
echo ✅ Entorno virtual activado correctamente.

:: Abre Visual Studio Code (opcional)
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe" (
    echo 🚀 Abriendo Visual Studio Code...
    start "" "C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe" .
) else (
    echo ⚠️ Visual Studio Code no encontrado. Puedes abrirlo manualmente si lo usas.
)

:: Mantiene la ventana abierta
cmd /k

