class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para efetuar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

titular = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(titular,5000)
print(" 1. Depositar \n 2. Sacar")
opcao = input("digite uma das opções :")
if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor)
elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor)
else:
    print("opção inválida")