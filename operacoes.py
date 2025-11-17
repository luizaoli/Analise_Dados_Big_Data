# operacoes.py

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(base, expoente):
    return base ** expoente


def raiz(radicando, indice=2):
    if indice == 0:
        raise ValueError("Índice da raiz não pode ser zero.")
    if radicando < 0 and indice % 2 == 0:
        raise ValueError("Não é possível calcular raiz par de número negativo (neste exemplo).")
    return radicando ** (1 / indice)


def porcentagem(base, taxa):
    # taxa em porcento (ex.: taxa=10 significa 10%)
    return base * (taxa / 100.0)
