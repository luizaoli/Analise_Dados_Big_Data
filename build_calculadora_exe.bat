@echo off
title Build Calculadora Interativa .exe
echo ============================================
echo   Gerador de executavel - Calculadora
echo ============================================
echo.

REM Certifique-se de rodar este arquivo DENTRO da pasta do projeto,
REM onde estao: interface_grafica.py, operacoes.py, historico.py, etc.

REM Opcional: se voce usa venv, ative antes de rodar este .bat:
REM   venv\Scripts\activate

echo Limpando pastas antigas (build, dist) e arquivo .spec...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist CalculadoraInterativa.spec del /f /q CalculadoraInterativa.spec

echo.
echo Gerando executavel com PyInstaller...

REM Se quiser sem icone, troque o comando abaixo por:
REM   pyinstaller --name CalculadoraInterativa --windowed --onefile interface_grafica.py

pyinstaller --name CalculadoraInterativa --windowed --onefile --icon=calculadora.ico interface_grafica.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Houve um erro ao gerar o executavel. Verifique as mensagens acima.
    echo Pressione qualquer tecla para sair...
    pause >nul
    exit /b %ERRORLEVEL%
)

echo.
echo Build concluido com sucesso!

if exist dist (
    echo Abrindo pasta "dist" com o executavel...
    start "" "dist"
)

echo.
echo Tudo pronto! O arquivo CalculadoraInterativa.exe esta dentro da pasta dist.
echo Pressione qualquer tecla para fechar esta janela...
pause >nul
