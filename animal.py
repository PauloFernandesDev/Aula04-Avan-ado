### Herança ###

class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O(A) {self.nome} foi comer...")

class Gato(Animal):
        def __init__(self,nome,cor):
            super().__init__(nome,cor)


        def miar(self):
            print(f"O(A) {self.nome}  miando...",)

class Coelho(Animal):
        def __init__(self,nome,cor):
            super().__init__(nome,cor)

        def pular(self):
            print(f"O(A) {self.nome} saiu pulando")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"O(A) {self.nome} foi mugir")

    def comer(self):
        print(f"O(A) {self.nome} foi comer capim")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O(A) {self.nome} saiu latindo")



