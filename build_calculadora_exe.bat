@echo off
title Gerar Executável da Calculadora Interativa
echo ================================================
echo   Construindo CalculadoraInterativa.exe
echo ================================================
echo.

REM Ativar o ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate

REM Verifica se o PyInstaller está instalado
echo Verificando PyInstaller...
pyinstaller --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo PyInstaller nao encontrado. Instalando...
    pip install pyinstaller
)

echo.
echo Gerando executavel...
pyinstaller --name CalculadoraInterativa --windowed --onefile --icon=calculadora.ico interface_grafica.py

echo.
echo Limpando arquivos temporarios...
del CalculadoraInterativa.spec 2>nul

echo.
echo Abrindo pasta dist...
start dist

echo.
echo Finalizado!
pause
