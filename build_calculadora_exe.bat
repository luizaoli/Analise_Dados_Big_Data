@echo off
setlocal
title Gerar Executável da Calculadora Interativa

echo ================================================
echo   Construindo CalculadoraInterativa.exe
echo ================================================
echo.

REM Garante que o script esta rodando na pasta do projeto
cd /d "%~dp0"

REM Ativar o ambiente virtual
echo Ativando ambiente virtual...
if exist "venv\Scripts\activate.bat" (
    call "venv\Scripts\activate.bat"
) else (
    echo Nao foi encontrado o ambiente virtual em "venv".
    echo Crie o venv com:  python -m venv venv
    echo E depois rode este script novamente.
    pause
    exit /b 1
)

REM Verifica se o PyInstaller esta instalado
echo.
echo Verificando PyInstaller...
pyinstaller --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo PyInstaller nao encontrado. Instalando...
    pip install pyinstaller
)

echo.
echo Gerando executavel...
pyinstaller --name CalculadoraInterativa --windowed --onefile --icon=calculadora.ico interface_grafica.py

REM Copiar o executavel gerado para a pasta raiz do projeto
echo.
if exist "dist\CalculadoraInterativa.exe" (
    echo Copiando executavel para a pasta do projeto...
    copy /Y "dist\CalculadoraInterativa.exe" ".\CalculadoraInterativa.exe" >nul
) else (
    echo Nao foi encontrado "dist\CalculadoraInterativa.exe".
    echo Verifique se o PyInstaller gerou o executavel corretamente.
)

REM Limpar arquivos e pastas temporarias de build
echo.
echo Limpando arquivos temporarios...
if exist build rd /s /q build
if exist dist rd /s /q dist
if exist CalculadoraInterativa.spec del /f /q CalculadoraInterativa.spec

echo.
echo ================================================
echo   Pronto! 
echo   O arquivo CalculadoraInterativa.exe
echo   esta na pasta do projeto.
echo ================================================
echo.
pause
endlocal