from contextlib import nullcontext


class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self,base,altura):
        self.area = base * altura
        print(f"Area do Retangulo: {self.area}")

    def calcularPerimetro(self,base,altura):
        self.perimetro = 2 * (base +altura)
        print(f"Perimetro do Retangulo: {self.perimetro}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self,base,altura):
        self.area = (base * altura)/2
        print(f"Area do Triangulo: {self.area}")

    def calcularPerimetro(self,base,altura):
        self.perimetro = base + altura
        print(f"Perimetro do Retangulo: {self.perimetro}")

