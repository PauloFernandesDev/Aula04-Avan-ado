class Ingresso():
    def __init__(self,valor):
        self.valor = valor
    def imprimeValor(self):
        print(f"Valor do Ingresso: {self.valor :.2f}")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor *= 1.5
    def imprimeValor(self):
        print(f"Valor do ingresso vip: {self.valor : .2f}")