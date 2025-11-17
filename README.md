
# 📘 Calculadora Interativa em Python  
Projeto desenvolvido por **Luiza de Oliveira Santos** para a disciplina de Python da **Pós‑Graduação da PUCPR**.  
A calculadora possui interface gráfica simples, porém funcional, histórico de operações, teclado numérico e suporte a tema claro/escuro.

O objetivo é demonstrar:
- domínio de Python  
- modularização do código  
- criação de executáveis  
- desenvolvimento de interfaces 

---

## 🧠 Como a calculadora funciona

A Calculadora Interativa foi criada em Python usando a biblioteca **Tkinter**, oferecendo:

### ✨ Funcionalidades principais
- **Operações básicas:** Soma, Subtração, Multiplicação e Divisão  
- **Operações avançadas:** Potência, Raiz e Porcentagem  
- **Histórico completo:** Todas as operações realizadas podem ser visualizadas  
- **Teclado numérico integrado:** Digitação prática através de botões  
- **Tema claro/escuro:** Alterne entre visual moderno escuro ou claro  
- **Resultado instantâneo:** Aperte Enter ou clique em *Calcular*

---

## 📂 Estrutura do Projeto

```
calculadora_interativa/
├─ interface_grafica.py      # Interface moderna com Tkinter
├─ interface_terminal.py     # Versão interativa no terminal
├─ operacoes.py              # Contém todas as funções matemáticas
├─ historico.py              # Gerencia o histórico de operações
├─ calculadora.ico           # Ícone utilizado no .exe
├─ build_calculadora_exe.bat # Script para montar o executável
└─ README.md
```

---

# 🚀 Como executar a calculadora

## 🔹 1. Executar diretamente pelo Python

### Interface gráfica:
```
python interface_grafica.py
```

### Interface de terminal:
```
python interface_terminal.py
```

---

# 💼 Criando o arquivo Executável (.exe)

Este projeto inclui um script especial (`.bat`) que automatiza a criação do executável Windows usando **PyInstaller**.

## 📄 O que o arquivo `.bat` faz?
O arquivo **build_calculadora_exe.bat**:

1. **Apaga versões antigas** (pastas `build/`, `dist/` e o `.spec`)  
2. **Gera um novo executável** em modo janela (sem console)  
3. Usa o ícone `calculadora.ico`  
4. **Abre automaticamente a pasta `dist/`** com o `.exe` pronto  

Você não precisa digitar comandos — o script faz tudo sozinho.

---

## ▶️ Como usar o arquivo `.bat`

1. Certifique-se de ter o **Python 3** e o **PyInstaller** instalado:
```
pip install pyinstaller
```

2. Coloque o arquivo **build_calculadora_exe.bat** dentro da pasta do projeto.

3. (Opcional) Ative seu ambiente virtual:
```
venv\Scriptsctivate
```

4. Clique duas vezes no arquivo:

```
build_calculadora_exe.bat
```

5. O script irá gerar:

```
dist/CalculadoraInterativa.exe
```

6. Abra esta pasta e execute o programa normalmente.

---

# 🖥️ Tecnologias Utilizadas
- Python 3  
- Tkinter (GUI)  
- PyInstaller (gerar .exe)  
- Pillow (opcional – usado apenas para criar GIFs)  

---



