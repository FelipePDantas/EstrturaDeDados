class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f" Olá {self.nome}, como vai?")

# Exemplo de uso da classe Pessoa
nomePessoa = input("Digite o nome da pessoa: ")
idadePessoa = int(input("Digite a idade da pessoa: "))

pessoa = Pessoa(nomePessoa, idadePessoa)
pessoa.falar()