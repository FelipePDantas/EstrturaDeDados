class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area



base = float(input("Digite a medida da base do retângulo: "))
altura = float(input("Digite a medida da altura do retângulo: "))

ret = Retangulo(base, altura)
print("\nA área do retângulo é:", ret.calcular_area())