# 📘 Calculadora Interativa em Python  

Projeto desenvolvido por **Luiza de Oliveira Santos** para a disciplina de **Python** do curso de **Pós-Graduação da PUCPR**.  
O objetivo é demonstrar o uso de Python com interface gráfica (Tkinter), organização em módulos, histórico de operações e empacotamento em executável `.exe`.

---

## 🧠 Visão geral da calculadora

A Calculadora Interativa possui:

- ✅ **Operações básicas:** soma, subtração, multiplicação e divisão  
- ✅ **Operações avançadas:** potência, raiz (com índice configurável) e porcentagem  
- ✅ **Interface gráfica moderna:** com tema claro/escuro, cards e teclado numérico  
- ✅ **Histórico de operações:** lista todas as operações realizadas, com possibilidade de limpar  
- ✅ **Teclado numérico integrado:** permite digitar pelos botões em vez do teclado físico  
- ✅ **Tema claro/escuro:** selecionável na própria interface  
- ✅ **Versão em modo texto (terminal):** para uso direto no console  

---

## 📂 Estrutura do projeto

```text
calculadora_interativa/
├─ interface_grafica.py        # Interface moderna com Tkinter (principal)
├─ interface_terminal.py       # Versão da calculadora no terminal
├─ operacoes.py                # Funções matemáticas (soma, divisão, etc.)
├─ historico.py                # Gerencia o histórico de operações
├─ calculadora.ico             # Ícone usado no executável .exe
├─ build_calculadora_exe.bat   # Script para gerar o executável Windows
├─ demo.gif                    # GIF de demonstração da calculadora
├─ .gitignore                  # Arquivos e pastas ignorados pelo Git
├─ README.md                   # Este arquivo
└─ docs/
   └─ manual_calculadora.md    # Manual de uso do projeto
```

---

## 🖱️ Como usar a calculadora (para professor(a) e colegas)

### 1️⃣ Clonar ou baixar o repositório

- Via Git (recomendado):
  ```bash
  git clone https://github.com/luizaoli/Analise_Dados_Big_Data.git
  ```

- Ou baixar como **ZIP**:
  - Acesse o repositório no GitHub  
  - Clique em **Code > Download ZIP**  
  - Extraia o ZIP em alguma pasta do computador

Depois, entre na pasta do projeto (por exemplo):

```bash
cd Analise_Dados_Big_Data
```

> Obs.: o nome da pasta local pode ser diferente se você renomear o projeto, o importante é manter os arquivos juntos.

---

## 🖥️ Executando a calculadora com Python

### ▶️ Interface gráfica (Tkinter)

Requisitos:
- Python 3 instalado (3.8+ recomendado)

No terminal (PowerShell/CMD) dentro da pasta do projeto:

```bash
python interface_grafica.py
```

A janela da calculadora será aberta com:

- Seleção de operação (soma, subtração, etc.)  
- Campos para **Número 1** e **Número 2**  
- Botão **Calcular**  
- Teclado numérico à direita  
- Histórico de operações na parte inferior  
- Combo para alternar o **tema (Escuro/Claro)**  
- Menu **Ajuda > Sobre**, com informações do projeto  

### ▶️ Interface de terminal

Se quiser usar no modo texto (sem interface gráfica):

```bash
python interface_terminal.py
```

A versão de terminal geralmente mostra um menu numerado, pedindo a escolha da operação e os valores.

---

## 💼 Gerando o executável `.exe` (Windows)

Este projeto já traz um arquivo especial: **`build_calculadora_exe.bat`**.  
Ele automatiza a criação de um executável da calculadora gráfica usando o **PyInstaller**.

### 🧩 O que o arquivo `.bat` faz?

Ao ser executado, o script:

1. Remove pastas antigas de build (`build/` e `dist/`, se existirem)  
2. Remove o arquivo `.spec` antigo (`CalculadoraInterativa.spec`, se existir)  
3. Roda o comando:
   ```bash
   pyinstaller --name CalculadoraInterativa --windowed --onefile --icon=calculadora.ico interface_grafica.py
   ```
4. Se tudo der certo, abre automaticamente a pasta `dist/`, onde estará o arquivo:
   ```text
   dist/CalculadoraInterativa.exe
   ```

Você pode então copiar esse `.exe` para outro computador com Windows e executar a calculadora sem precisar instalar Python.

### ▶️ Como usar o `.bat` passo a passo

1. Certifique-se de que o **Python 3** está instalado.  
2. Instale o **PyInstaller** (apenas na primeira vez):
   ```bash
   pip install pyinstaller
   ```
3. Dentro da pasta do projeto, dê dois cliques em:
   ```text
   build_calculadora_exe.bat
   ```
4. Aguarde o terminal terminar o processo.  
5. Ao final, a pasta **`dist`** será aberta automaticamente.  
6. Dentro dela, procure pelo arquivo:
   ```text
   CalculadoraInterativa.exe
   ```
7. Execute-o normalmente (pode até fixar na barra de tarefas 😉).

---

## 📘 Manual de uso (resumo)

Um manual mais detalhado está disponível em:  
`docs/manual_calculadora.md`

Ele explica:

- Estrutura do código
- Fluxo interno da interface gráfica
- Como o histórico de operações é armazenado
- Como funciona o teclado numérico
- Sugestões de expansão futura

Você pode abrir esse arquivo em qualquer editor de texto ou IDE, ou convertê-lo para PDF usando Word, LibreOffice ou ferramentas online, se necessário para entrega formal.

---

## 🛠️ Tecnologias utilizadas

- **Python 3** – linguagem principal do projeto  
- **Tkinter** – construção da interface gráfica (GUI)  
- **PyInstaller** – empacotamento em executável `.exe` para Windows  
- **Git + GitHub** – controle de versão e publicação do código  
- **Pillow** (opcional) – utilizado apenas no processo de criação de GIFs demonstrativos (não é necessário para rodar o app)  

---

## 🔮 Possíveis melhorias futuras

- Adicionar novas operações (logaritmos, trigonometria, conversões, etc.)  
- Implementar verificação mais robusta de erros (ex.: divisão por zero customizada)  
- Criar suporte a múltiplas línguas (português/inglês)  
- Exportar histórico para arquivos `.csv` ou `.txt`  
- Adicionar testes automatizados com `pytest`  

---

## 👩‍🎓 Sobre o projeto

Este projeto foi desenvolvido por **Luiza de Oliveira Santos** para a disciplina de Python no curso de **Pós-Graduação da PUCPR**.

Ele demonstra:

- Organização de código em módulos (separação de interface, lógica e histórico)  
- Uso de interface gráfica com Tkinter em Python  
- Criação de executáveis para Windows  
- Boas práticas de documentação e versionamento de código (Git/GitHub)  

Se você está corrigindo, avaliando ou estudando este projeto, sinta-se à vontade para:

- Clonar o repositório  
- Executar a calculadora  
- Explorar o código  
- Sugerir melhorias ou abrir *Issues* no GitHub 😊

---
