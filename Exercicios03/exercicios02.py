def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
        print(fatorial)
    return fatorial


numero = int(input("Digite um número inteiro positivo: "))

resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")