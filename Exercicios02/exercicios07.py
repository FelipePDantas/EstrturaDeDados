class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

marca_carro = input("Digite a marca do carro: ")
modelo_carro = input("Digite o modelo do carro: ")
ano_carro = int(input("Digite o ano do carro: "))

carro = Carro(marca_carro, modelo_carro, ano_carro)
print("Detalhes do carro:")
print(carro.detalhes())