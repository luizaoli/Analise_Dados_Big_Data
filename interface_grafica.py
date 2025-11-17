# interface_grafica.py

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

from operacoes import somar, subtrair, multiplicar, dividir, potencia, raiz, porcentagem
from historico import HistoricoOperacoes


# Paletas de tema
PALETA_ESCURO = {
    "fundo": "#020617",
    "fundo_card": "#020617",
    "fundo_card2": "#020617",
    "texto": "#e5e7eb",
    "texto_suave": "#9ca3af",
    "acento": "#38bdf8",
    "acento_clara": "#0ea5e9",
    "borda_card": "#1e293b",
    "list_bg": "#020617",
    "list_sel": "#0f172a",
}

PALETA_CLARO = {
    "fundo": "#f3f4f6",
    "fundo_card": "#ffffff",
    "fundo_card2": "#e5f2ff",
    "texto": "#111827",
    "texto_suave": "#6b7280",
    "acento": "#2563eb",
    "acento_clara": "#3b82f6",
    "borda_card": "#d1d5db",
    "list_bg": "#ffffff",
    "list_sel": "#dbeafe",
}

VERSAO_APP = "Calculadora Interativa v1.0"
AUTOR_APP = "Autor: Luiza de Oliveira Santos"


def obter_caminho_recurso(caminho_relativo: str) -> str:
    """
    Retorna o caminho absoluto de um recurso (ícone, imagem, etc.),
    funcionando tanto no modo normal (.py) quanto no executável (.exe) gerado pelo PyInstaller.
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS  # quando empacotado pelo PyInstaller
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, caminho_relativo)


def executar_interface_grafica():
    historico = HistoricoOperacoes()
    paleta_atual = {"valor": PALETA_ESCURO}
    last_entry_focus = {"widget": None}

    def aplicar_tema(paleta: dict):
        paleta_atual["valor"] = paleta
        p = paleta

        janela.configure(bg=p["fundo"])

        estilo.configure("Raiz.TFrame", background=p["fundo"])

        estilo.configure(
            "Card.TLabelframe",
            background=p["fundo_card"],
            foreground=p["texto"],
            bordercolor=p["borda_card"],
            relief="solid",
            borderwidth=1,
        )
        estilo.configure(
            "Card.TLabelframe.Label",
            background=p["fundo_card"],
            foreground=p["texto_suave"],
            font=("Segoe UI", 9, "bold"),
        )

        estilo.configure(
            "Card2.TLabelframe",
            background=p["fundo_card2"],
            foreground=p["texto"],
            bordercolor=p["borda_card"],
            relief="solid",
            borderwidth=1,
        )
        estilo.configure(
            "Card2.TLabelframe.Label",
            background=p["fundo_card2"],
            foreground=p["texto_suave"],
            font=("Segoe UI", 9, "bold"),
        )

        estilo.configure("Titulo.TLabel", font=("Segoe UI Semibold", 18, "bold"), foreground=p["texto"], background=p["fundo"])
        estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 10), foreground=p["texto_suave"], background=p["fundo"])
        estilo.configure("Texto.TLabel", font=("Segoe UI", 10), foreground=p["texto"], background=p["fundo_card"])
        estilo.configure("TextoCard2.TLabel", font=("Segoe UI", 10), foreground=p["texto"], background=p["fundo_card2"])
        estilo.configure("Resultado.TLabel", font=("Segoe UI Semibold", 18, "bold"), foreground=p["acento_clara"], background=p["fundo_card2"])
        estilo.configure("Status.TLabel", font=("Segoe UI", 9), foreground=p["texto_suave"], background=p["fundo"])

        estilo.configure(
            "BotaoPrincipal.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            foreground="#0b1120" if p is PALETA_ESCURO else "#f9fafb",
            background=p["acento"],
            borderwidth=0,
            focusthickness=3,
            focuscolor=p["acento_clara"],
        )
        estilo.map(
            "BotaoPrincipal.TButton",
            background=[("active", p["acento_clara"]), ("pressed", p["acento_clara"])],
            foreground=[("disabled", "#6b7280")],
        )

        estilo.configure(
            "BotaoSecundario.TButton",
            font=("Segoe UI", 9),
            padding=6,
            foreground=p["texto"],
            background="#111827" if p is PALETA_ESCURO else "#e5e7eb",
            borderwidth=0,
        )
        estilo.map(
            "BotaoSecundario.TButton",
            background=[("active", "#1f2937" if p is PALETA_ESCURO else "#d1d5db"), ("pressed", p["fundo"])],
            foreground=[("disabled", "#6b7280")],
        )

        estilo.configure(
            "TCombobox",
            fieldbackground=p["fundo_card"],
            background=p["fundo_card"],
            foreground=p["texto"],
            bordercolor=p["borda_card"],
            arrowsize=14,
        )
        estilo.map(
            "TCombobox",
            fieldbackground=[("readonly", p["fundo_card"])],
            selectbackground=[("readonly", p["fundo_card"])],
            selectforeground=[("readonly", p["texto"])],
        )
        estilo.configure(
            "TEntry",
            fieldbackground=p["fundo_card"],
            background=p["fundo_card"],
            foreground=p["texto"],
            bordercolor=p["borda_card"],
            insertcolor=p["acento"],
        )

        lista_historico.config(
            bg=p["list_bg"],
            fg=p["texto"],
            selectbackground=p["list_sel"],
            selectforeground=p["texto"],
        )

    def calcular():
        operacao_selecionada = combo_operacao.get()

        texto_num1 = entrada_num1.get().strip()
        texto_num2 = entrada_num2.get().strip()

        try:
            num1 = float(texto_num1)
        except ValueError:
            messagebox.showerror("Erro", "Primeiro número inválido.")
            entrada_num1.focus()
            return

        try:
            if operacao_selecionada == "Raiz":
                if texto_num2 == "":
                    indice = 2.0
                else:
                    indice = float(texto_num2)
                resultado = raiz(num1, indice)
                descricao = f"Raiz de índice {indice} de {num1}"
                historico.adicionar("Raiz", [num1, indice], resultado)
            else:
                if texto_num2 == "":
                    messagebox.showerror("Erro", "Informe o segundo número.")
                    entrada_num2.focus()
                    return

                num2 = float(texto_num2)

                if operacao_selecionada == "Somar":
                    resultado = somar(num1, num2)
                    descricao = f"{num1} + {num2}"
                    historico.adicionar("Soma", [num1, num2], resultado)
                elif operacao_selecionada == "Subtrair":
                    resultado = subtrair(num1, num2)
                    descricao = f"{num1} - {num2}"
                    historico.adicionar("Subtração", [num1, num2], resultado)
                elif operacao_selecionada == "Multiplicar":
                    resultado = multiplicar(num1, num2)
                    descricao = f"{num1} * {num2}"
                    historico.adicionar("Multiplicação", [num1, num2], resultado)
                elif operacao_selecionada == "Dividir":
                    resultado = dividir(num1, num2)
                    descricao = f"{num1} / {num2}"
                    historico.adicionar("Divisão", [num1, num2], resultado)
                elif operacao_selecionada == "Potência":
                    resultado = potencia(num1, num2)
                    descricao = f"{num1} ^ {num2}"
                    historico.adicionar("Potência", [num1, num2], resultado)
                elif operacao_selecionada == "Porcentagem":
                    resultado = porcentagem(num1, num2)
                    descricao = f"{num2}% de {num1}"
                    historico.adicionar("Porcentagem", [num1, num2], resultado)
                else:
                    messagebox.showerror("Erro", "Selecione uma operação válida.")
                    return

            rotulo_resultado_valor.config(text=str(resultado))
            atualizar_lista_historico()
            atualizar_status(f"Última operação: {descricao} = {resultado}")
        except ValueError as erro:
            messagebox.showerror("Erro na operação", str(erro))

    def atualizar_lista_historico():
        lista_historico.delete(0, tk.END)
        for registro in historico.listar():
            lista_historico.insert(tk.END, registro.formatar())

    def limpar_historico():
        historico.limpar()
        atualizar_lista_historico()
        atualizar_status("Histórico limpo.")

    def ao_mudar_operacao(event=None):
        operacao = combo_operacao.get()
        if operacao == "Raiz":
            rotulo_num2.config(text="Índice da raiz (padrão: 2):")
            atualizar_status("Dica: se deixar o índice vazio, será usada a raiz quadrada.")
        elif operacao == "Porcentagem":
            rotulo_num2.config(text="Taxa (%):")
            atualizar_status("Exemplo: Número 1 = 200, Taxa = 10 → 10% de 200.")
        else:
            rotulo_num2.config(text="Número 2:")
            atualizar_status("Informe dois números e clique em Calcular.")

    def atalho_enter(event):
        calcular()

    def atualizar_status(texto):
        rotulo_status.config(text=texto)

    def on_focus_entry(event):
        last_entry_focus["widget"] = event.widget

    def teclado_inserir(valor: str):
        entry = last_entry_focus.get("widget")
        if entry is None or not hasattr(entry, "insert"):
            entry = entrada_num1

        if valor == "C":
            entry.delete(0, tk.END)
        elif valor == "←":
            atual = entry.get()
            if atual:
                entry.delete(len(atual) - 1, tk.END)
        else:
            entry.insert(tk.END, valor)

        entry.focus()

    def alterar_tema(event=None):
        escolha = combo_tema.get()
        if escolha == "Escuro":
            aplicar_tema(PALETA_ESCURO)
        else:
            aplicar_tema(PALETA_CLARO)

    def mostrar_sobre():
        mensagem = f"{VERSAO_APP}\n{AUTOR_APP}\n\nProjeto de estudo em Python + Tkinter."
        messagebox.showinfo("Sobre", mensagem)

    # Janela principal
    janela = tk.Tk()
    janela.title("Calculadora Interativa")
    janela.minsize(620, 500)
    janela.resizable(True, True)

    # janela.iconbitmap(obter_caminho_recurso("calculadora.ico"))

    janela.update_idletasks()
    largura = 780
    altura = 520
    pos_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    pos_y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    # Menu
    barra_menu = tk.Menu(janela)
    menu_ajuda = tk.Menu(barra_menu, tearoff=0)
    menu_ajuda.add_command(label="Sobre", command=mostrar_sobre)
    barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
    janela.config(menu=barra_menu)

    global estilo
    estilo = ttk.Style()
    try:
        estilo.theme_use("clam")
    except tk.TclError:
        pass

    frame_raiz = ttk.Frame(janela, padding=16, style="Raiz.TFrame")
    frame_raiz.grid(row=0, column=0, sticky="nsew")

    frame_titulo = ttk.Frame(frame_raiz, style="Raiz.TFrame")
    frame_titulo.grid(row=0, column=0, sticky="ew")
    frame_titulo.columnconfigure(0, weight=1)
    frame_titulo.columnconfigure(1, weight=0)

    rotulo_titulo = ttk.Label(frame_titulo, text="Calculadora Interativa", style="Titulo.TLabel")
    rotulo_titulo.grid(row=0, column=0, sticky="w")

    frame_tema = ttk.Frame(frame_titulo, style="Raiz.TFrame")
    frame_tema.grid(row=0, column=1, sticky="e")

    lbl_tema = ttk.Label(frame_tema, text="Tema:", style="Subtitulo.TLabel")
    lbl_tema.grid(row=0, column=0, sticky="e", padx=(0, 4))

    combo_tema = ttk.Combobox(
        frame_tema,
        values=["Escuro", "Claro"],
        state="readonly",
        width=8,
    )
    combo_tema.current(0)
    combo_tema.grid(row=0, column=1, sticky="e")
    combo_tema.bind("<<ComboboxSelected>>", alterar_tema)

    rotulo_subtitulo = ttk.Label(
        frame_raiz,
        text="Escolha a operação, informe os números e acompanhe o resultado e o histórico.",
        style="Subtitulo.TLabel",
        wraplength=520,
    )
    rotulo_subtitulo.grid(row=1, column=0, sticky="w", pady=(4, 12))

    frame_superior = ttk.Frame(frame_raiz, style="Raiz.TFrame")
    frame_superior.grid(row=2, column=0, sticky="nsew")
    frame_raiz.rowconfigure(2, weight=2)
    frame_superior.columnconfigure(0, weight=3)
    frame_superior.columnconfigure(1, weight=2)
    frame_superior.columnconfigure(2, weight=2)

    frame_operacao = ttk.LabelFrame(frame_superior, text=" Operação e números ", padding=12, style="Card.TLabelframe")
    frame_operacao.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
    frame_operacao.columnconfigure(1, weight=1)

    lbl_op = ttk.Label(frame_operacao, text="Operação:", style="Texto.TLabel")
    lbl_op.grid(row=0, column=0, sticky="w")
    combo_operacao = ttk.Combobox(
        frame_operacao,
        values=["Somar", "Subtrair", "Multiplicar", "Dividir", "Potência", "Raiz", "Porcentagem"],
        state="readonly",
        width=18,
    )
    combo_operacao.current(0)
    combo_operacao.grid(row=0, column=1, sticky="ew", pady=4)

    lbl_n1 = ttk.Label(frame_operacao, text="Número 1:", style="Texto.TLabel")
    lbl_n1.grid(row=1, column=0, sticky="w", pady=(6, 0))
    entrada_num1 = ttk.Entry(frame_operacao, width=20)
    entrada_num1.grid(row=1, column=1, sticky="ew", pady=(6, 0))

    rotulo_num2 = ttk.Label(frame_operacao, text="Número 2:", style="Texto.TLabel")
    rotulo_num2.grid(row=2, column=0, sticky="w", pady=(6, 0))
    entrada_num2 = ttk.Entry(frame_operacao, width=20)
    entrada_num2.grid(row=2, column=1, sticky="ew", pady=(6, 0))

    botao_calcular = ttk.Button(
        frame_operacao,
        text="Calcular",
        style="BotaoPrincipal.TButton",
        command=calcular,
    )
    botao_calcular.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(12, 0))

    frame_resultado = ttk.LabelFrame(frame_superior, text=" Resultado ", padding=12, style="Card2.TLabelframe")
    frame_resultado.grid(row=0, column=1, sticky="nsew")
    frame_resultado.columnconfigure(0, weight=1)

    lbl_resultado = ttk.Label(frame_resultado, text="Resultado:", style="TextoCard2.TLabel")
    lbl_resultado.grid(row=0, column=0, sticky="w")
    rotulo_resultado_valor = ttk.Label(frame_resultado, text="–", style="Resultado.TLabel")
    rotulo_resultado_valor.grid(row=1, column=0, sticky="w", pady=(8, 0))

    frame_teclado = ttk.LabelFrame(frame_superior, text=" Teclado numérico ", padding=12, style="Card.TLabelframe")
    frame_teclado.grid(row=0, column=2, sticky="nsew", padx=(10, 0))

    for c in range(4):
        frame_teclado.columnconfigure(c, weight=1)

    # Layout do teclado:
    #  7  8  9  ←
    #  4  5  6  C
    #  1  2  3  .
    #  0  (ocupa duas colunas)
    botoes = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("←", 0, 3),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("C", 1, 3),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), (".", 2, 3),
        ("0", 3, 0),
    ]

    for texto, linha, coluna in botoes:
        btn = ttk.Button(
            frame_teclado,
            text=texto,
            style="BotaoSecundario.TButton",
            command=lambda v=texto: teclado_inserir(v),
        )
        if texto == "0":
            btn.grid(row=linha, column=coluna, columnspan=2, sticky="nsew", padx=2, pady=2, ipady=4)
        else:
            btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2, ipady=4)

    for i in range(4):
        frame_teclado.rowconfigure(i, weight=1, minsize=36)

    frame_historico = ttk.LabelFrame(frame_raiz, text=" Histórico de operações ", padding=12, style="Card.TLabelframe")
    frame_historico.grid(row=3, column=0, sticky="nsew", pady=(12, 6))
    frame_raiz.rowconfigure(3, weight=3)
    frame_historico.rowconfigure(0, weight=1)
    frame_historico.columnconfigure(0, weight=1)

    frame_historico_inner = ttk.Frame(frame_historico, style="Card.TLabelframe")
    frame_historico_inner.grid(row=0, column=0, sticky="nsew")
    frame_historico_inner.rowconfigure(0, weight=1)
    frame_historico_inner.columnconfigure(0, weight=1)

    lista_historico = tk.Listbox(
        frame_historico_inner,
        height=8,
        highlightthickness=0,
        border=0,
        activestyle="none",
    )
    lista_historico.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(frame_historico_inner, orient="vertical", command=lista_historico.yview)
    lista_historico.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns", padx=(6, 0))

    botao_limpar_historico = ttk.Button(
        frame_historico,
        text="Limpar histórico",
        style="BotaoSecundario.TButton",
        command=limpar_historico,
    )
    botao_limpar_historico.grid(row=1, column=0, sticky="e", pady=(10, 0))

    rotulo_status = ttk.Label(frame_raiz, text="Pronto.", style="Status.TLabel")
    rotulo_status.grid(row=4, column=0, sticky="w", pady=(4, 0))

    janela.rowconfigure(0, weight=1)
    janela.columnconfigure(0, weight=1)
    frame_raiz.columnconfigure(0, weight=1)
    frame_superior.rowconfigure(0, weight=1)

    combo_operacao.bind("<<ComboboxSelected>>", ao_mudar_operacao)
    janela.bind("<Return>", atalho_enter)
    entrada_num1.bind("<FocusIn>", on_focus_entry)
    entrada_num2.bind("<FocusIn>", on_focus_entry)

    aplicar_tema(PALETA_ESCURO)

    entrada_num1.focus()
    ao_mudar_operacao()

    janela.mainloop()


if __name__ == "__main__":
    try:
        executar_interface_grafica()
    except Exception as erro:
        try:
            messagebox.showerror("Erro crítico", f"Ocorreu um erro inesperado:\n{erro}")
        except Exception:
            print("Erro crítico ao executar a aplicação:", erro)