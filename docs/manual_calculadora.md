# Manual da Calculadora Interativa em Python

Projeto desenvolvido por **Luiza de Oliveira Santos** para a disciplina de Python da **Pós-Graduação da PUCPR**.

---

## 1. Objetivo do projeto

A Calculadora Interativa tem como objetivo demonstrar:

- Uso de Python com **Tkinter** para criação de interfaces gráficas
- Separação de responsabilidades em módulos (`operacoes.py`, `historico.py`, etc.)
- Utilização de histórico de operações
- Criação de executável Windows usando **PyInstaller**
- Boas práticas de organização e documentação de código

---

## 2. Arquitetura do sistema

### 2.1. Módulos principais

- **`interface_grafica.py`**  
  Responsável pela interface visual da calculadora.  
  Principais elementos:
  - Seleção da operação (combobox)
  - Campos de entrada de números
  - Botão de calcular
  - Teclado numérico
  - Histórico de operações
  - Seleção de tema (claro/escuro)
  - Menu "Ajuda > Sobre"

- **`interface_terminal.py`**  
  Versão alternativa do projeto para uso via terminal/console.  
  Permite escolher operações por menu e digitar valores diretamente.

- **`operacoes.py`**  
  Contém funções matemáticas desacopladas da interface, como:
  - `somar(a, b)`
  - `subtrair(a, b)`
  - `multiplicar(a, b)`
  - `dividir(a, b)`
  - `potencia(base, expoente)`
  - `raiz(numero, indice)`
  - `porcentagem(valor, taxa)`

- **`historico.py`**  
  Implementa uma classe para armazenar e listar operações realizadas.  
  Pode usar `dataclasses` para organizar os dados de cada operação.

---

## 3. Fluxo de funcionamento da interface gráfica

1. O usuário seleciona uma **operação** (ex.: "Somar") no combobox.  
2. Preenche os campos **Número 1** e **Número 2** (quando necessário).  
3. Clica em **Calcular** ou pressiona **Enter**.  
4. A função `calcular()`:
   - Lê os valores dos campos
   - Converte para `float`
   - Chama a função adequada em `operacoes.py`
   - Atualiza o rótulo de **Resultado**
   - Registra a operação no **histórico**
5. O histórico é exibido em uma `Listbox` na parte inferior da tela.  
6. O usuário pode limpar o histórico clicando em **"Limpar histórico"**.  
7. O usuário também pode alternar o **tema** (Escuro/Claro) na parte superior direita.  

---

## 4. Teclado numérico

O teclado numérico é exibido na lateral direita da interface gráfica.

- Botões disponíveis:
  - `7 8 9 ←`
  - `4 5 6 C`
  - `1 2 3 .`
  - `0` (ocupando duas colunas)

- Funcionalidade:
  - O teclado insere dígitos no último campo de texto que recebeu foco (`Número 1` ou `Número 2`)
  - `C` limpa completamente o campo atual
  - `←` apaga o último caractere
  - `.` adiciona casa decimal

Isso facilita o uso em ambientes com toque (touchscreen) ou onde o usuário prefere clicar nos botões da tela.

---

## 5. Histórico de operações

Cada operação realizada é salva em uma estrutura de histórico.  
Isso permite que o usuário veja:

- Qual operação foi feita
- Quais valores foram usados
- Qual foi o resultado

O histórico pode ser limpo a qualquer momento pelo botão **"Limpar histórico"**.

---

## 6. Geração de executável (.exe)

A calculadora foi preparada para ser empacotada como um executável Windows usando o **PyInstaller**.

- O arquivo `build_calculadora_exe.bat` automatiza o processo:
  - Limpa builds antigos
  - Gera um novo `.exe`
  - Usa o ícone `calculadora.ico`
  - Abre a pasta `dist/` ao final

Isso é útil para distribuição para usuários que não têm Python instalado.

---

## 7. Como utilizar este projeto em contexto acadêmico

Sugestões de uso em sala ou em avaliações:

- Analisar a separação entre **interface** e **lógica de negócio**
- Propor novas operações (ex.: módulo, exponencial, fatorial)
- Implementar tratamento de erros adicionais (divisão por zero, entrada vazia, etc.)
- Criar testes unitários para o módulo `operacoes.py`
- Adaptar a interface para outros contextos (ex.: calculadora financeira)

---

## 8. Créditos

Projeto desenvolvido por **Luiza de Oliveira Santos**  
Para a disciplina de Python – **Pós-Graduação PUCPR**.

---

Este manual pode ser convertido para PDF se desejado, usando:
- Microsoft Word
- LibreOffice Writer
- Ferramentas online de conversão de Markdown/Texto para PDF
