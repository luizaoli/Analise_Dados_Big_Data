# 📘 Calculadora Interativa em Python  

Projeto desenvolvido por **Luiza de Oliveira Santos** para a disciplina de **Python** no curso de **Pós-Graduação da PUCPR**.  
Esta calculadora possui interface gráfica moderna, histórico de operações e capacidade de exportação para um executável `.exe` via PyInstaller.

---

## 🧠 Visão geral da calculadora

A Calculadora Interativa oferece:

- ✔️ **Operações básicas:** soma, subtração, multiplicação, divisão  
- ✔️ **Operações avançadas:** potência, raiz e porcentagem  
- ✔️ **Interface gráfica moderna:** tema claro/escuro, teclado numérico, cards e feedback visual  
- ✔️ **Histórico de operações:** listagem e limpeza de histórico  
- ✔️ **Botão “Limpar campos”** para reiniciar os campos de entrada  
- ✔️ **Modo terminal** (interface de texto)  
- ✔️ **Geração automática de executável `.exe`** para Windows  

---

## 📂 Estrutura do projeto

```
calculadora_interativa/
├─ interface_grafica.py
├─ interface_terminal.py
├─ operacoes.py
├─ historico.py
├─ calculadora.ico
├─ build_calculadora_exe.bat
├─ CalculadoraInterativa.exe
├─ README.md
└─ docs/
   └─ manual_calculadora.md
```

Pastas temporárias removidas automaticamente pelo .bat:

- build/  
- dist/  
- *.spec  
- __pycache__/  

---

## 🖥️ Como executar a calculadora

### ▶️ Interface gráfica

```
python interface_grafica.py
```

### ▶️ Interface terminal

```
python interface_terminal.py
```

---

## 🧩 Funcionalidades da interface gráfica

- seleção de operação  
- campos de entrada  
- botão Calcular  
- botão Limpar campos  
- teclado numérico  
- histórico de operações  
- tema claro/escuro  
- menu Ajuda → Sobre  

---

# 💼 Geração do executável `.exe` (Windows)

Use o arquivo:

```
build_calculadora_exe.bat
```

Ele agora:

- ativa o venv  
- instala PyInstaller se faltar  
- gera o .exe  
- move o .exe para a pasta principal  
- remove build/, dist/ e .spec  

---

## ▶️ Como usar

1. Criar venv:
```
python -m venv venv
```
2. Rodar:
```
build_calculadora_exe.bat
```

O executável final ficará em:

```
CalculadoraInterativa.exe
```

---

## 👩‍🎓 Sobre o projeto

Desenvolvido por **Luiza de Oliveira Santos**  
Curso: Pós-Graduação PUCPR  
Disciplina: Python
