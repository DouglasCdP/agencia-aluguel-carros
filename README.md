# agencia-aluguel-carros
from abc import ABC, abstractmethod

class Alugavel(ABC):
    @abstractmethod
    def calcular_preco(self, dias: int) -> float:
        pass

    @abstractmethod
    def exibir_detalhes(self):
        pass
