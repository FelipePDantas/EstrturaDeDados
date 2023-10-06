import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        return area


raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
area = circulo.calcular_area()
print(f"A área do círculo com raio {raio} é {area:.2f}")