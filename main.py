from animal import *
from ingresso import *
from forma  import *

gato = Gato("lulu","preto")
cachorro = Cachorro("Toddy","branco")
coelho = Coelho("Pernafina","transparente")
vaca = Vaca("melosa","marron")

gato.miar()
gato.comer()
cachorro.latir()
coelho.pular()
vaca.mugir()
vaca.comer()

print("*********************************")
cinema = Ingresso(20)
cinemavip = Vip(20)

cinema.imprimeValor()
cinemavip.imprimeValor()

print("*********************************")

triangulo = Triangulo()
retangulo = Retangulo()

triangulo.calcularArea(3,5)
triangulo.calcularPerimetro(3,5)
print("*********************************")
retangulo.calcularArea(3,5)
retangulo.calcularPerimetro(3,5)
