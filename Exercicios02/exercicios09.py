class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Exemplo de uso da classe Triangulo
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

triangulo = Triangulo(lado1, lado2, lado3)
perimetro = triangulo.calcular_perimetro()
print(f"O perímetro do triângulo é {perimetro:.2f}")