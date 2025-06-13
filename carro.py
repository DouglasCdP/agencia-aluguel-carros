from veiculo_interface import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.alugado = False

    def alugar(self):
        if not self.alugado:
            self.alugado = True
            print(f"Carro {self.modelo} alugado com sucesso.")
        else:
            print(f"Carro {self.modelo} já está alugado.")

    def devolver(self):
        if self.alugado:
            self.alugado = False
            print(f"Carro {self.modelo} devolvido com sucesso.")
        else:
            print(f"Carro {self.modelo} não está alugado.")

    def exibir_informacoes(self):
        status = "Alugado" if self.alugado else "Disponível"
        print(f"Carro: {self.modelo} | Placa: {self.placa} | Status: {status}")