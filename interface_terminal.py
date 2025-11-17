# interface_terminal.py

from operacoes import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    raiz,
    porcentagem,
)
from historico import HistoricoOperacoes


def mostrar_menu():
    print("\n===== CALCULADORA INTERATIVA (TERMINAL) =====")
    print("1) Somar")
    print("2) Subtrair")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Potência")
    print("6) Raiz")
    print("7) Porcentagem")
    print("8) Ver histórico")
    print("9) Limpar histórico")
    print("0) Sair")


def ler_numero(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def executar_interface_terminal():
    historico = HistoricoOperacoes()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo da calculadora. Até mais!")
            break

        if opcao == "8":
            registros = historico.listar()
            if not registros:
                print("\nHistórico vazio.")
            else:
                print("\n===== HISTÓRICO DE OPERAÇÕES =====")
                for registro in registros:
                    print(registro.formatar())
            continue

        if opcao == "9":
            historico.limpar()
            print("Histórico limpo.")
            continue

        if opcao in {"1", "2", "3", "4", "5", "7"}:
            numero1 = ler_numero("Digite o primeiro número: ")
            numero2 = ler_numero("Digite o segundo número: ")

            try:
                if opcao == "1":
                    resultado = somar(numero1, numero2)
                    operacao = f"{numero1} + {numero2}"
                    nome_operacao = "Soma"
                elif opcao == "2":
                    resultado = subtrair(numero1, numero2)
                    operacao = f"{numero1} - {numero2}"
                    nome_operacao = "Subtração"
                elif opcao == "3":
                    resultado = multiplicar(numero1, numero2)
                    operacao = f"{numero1} * {numero2}"
                    nome_operacao = "Multiplicação"
                elif opcao == "4":
                    resultado = dividir(numero1, numero2)
                    operacao = f"{numero1} / {numero2}"
                    nome_operacao = "Divisão"
                elif opcao == "5":
                    resultado = potencia(numero1, numero2)
                    operacao = f"{numero1} ^ {numero2}"
                    nome_operacao = "Potência"
                else:  # opcao == "7"
                    resultado = porcentagem(numero1, numero2)
                    operacao = f"{numero2}% de {numero1}"
                    nome_operacao = "Porcentagem"

                print(f"\nResultado: {operacao} = {resultado}")
                historico.adicionar(nome_operacao, [numero1, numero2], resultado)

            except ValueError as erro:
                print(f"Erro na operação: {erro}")

        elif opcao == "6":
            radicando = ler_numero("Digite o radicando (número dentro da raiz): ")
            entrada_indice = input("Digite o índice da raiz (2 para raiz quadrada, pressione Enter para 2): ").strip()
            if entrada_indice == "":
                indice = 2.0
            else:
                try:
                    indice = float(entrada_indice)
                except ValueError:
                    print("Índice inválido. Usando 2 como padrão.")
                    indice = 2.0

            try:
                resultado = raiz(radicando, indice)
                print(f"\nResultado: raiz de índice {indice} de {radicando} = {resultado}")
                historico.adicionar("Raiz", [radicando, indice], resultado)
            except ValueError as erro:
                print(f"Erro na operação: {erro}")

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar_interface_terminal()
