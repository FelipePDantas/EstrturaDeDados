class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    # Método para aumentar o salário do funcionário por um percentual
    def aumentar_salario(self, percentual_aumento):
        self.salario += (self.salario * percentual_aumento)
        return self.salario

# Exemplo de uso da classe Funcionario
nomeFuncionario = input("Digite o nome do funcionário: ")
salarioFuncionario = float(input("Digite o salário do funcionário: "))
cargoFuncionario = input("Digite o cargo do funcionário: ")

funcionario = Funcionario(nomeFuncionario,salarioFuncionario,cargoFuncionario)
atualizado = funcionario.aumentar_salario(0.1)

print(f"f o valor do salário é {atualizado}")