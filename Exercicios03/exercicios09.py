def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "nao pode ser dividido por zero"
    return x / y

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Digite o número da operação desejada: "))

if opcao in [1, 2, 3, 4]:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = somar(numero1, numero2)
        operacao = "adição"
    elif opcao == 2:
        resultado = subtrair(numero1, numero2)
        operacao = "subtração"
    elif opcao == 3:
        resultado = multiplicar(numero1, numero2)
        operacao = "multiplicação"
    else:
        resultado = dividir(numero1, numero2)
        operacao = "divisão"

    print(f"O resultado da {operacao} é: {resultado}")
else:
    print("Opção inválida. Por favor, escolha uma operação de 1 a 4.")