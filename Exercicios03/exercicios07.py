def calcular_imc(peso, altura):

    if peso <= 0 or altura <= 0:
        return "Peso e altura devem ser valores positivos."
    else:
        imc = peso / (altura ** 2)
        return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

resultado_imc = calcular_imc(peso, altura)
print("Seu Índice de Massa Corporal (IMC) é {:.2f}".format(resultado_imc))