# historico.py
from dataclasses import dataclass
from typing import List


@dataclass
class RegistroOperacao:
    operacao: str
    operandos: List[float]
    resultado: float

    def formatar(self) -> str:
        operandos_str = ", ".join(str(op) for op in self.operandos)
        return f"{self.operacao}: ({operandos_str}) = {self.resultado}"


class HistoricoOperacoes:
    def __init__(self):
        self._registros: List[RegistroOperacao] = []

    def adicionar(self, operacao: str, operandos: List[float], resultado: float) -> None:
        registro = RegistroOperacao(operacao=operacao, operandos=operandos, resultado=resultado)
        self._registros.append(registro)

    def listar(self) -> List[RegistroOperacao]:
        return list(self._registros)

    def limpar(self) -> None:
        self._registros.clear()
