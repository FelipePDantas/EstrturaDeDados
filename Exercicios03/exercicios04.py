def soma_digitos(numero):
    soma = 0
    while numero > 0:

        digito = numero % 10
        soma += digito
        numero = numero // 10
    return soma


numero = int(input("Digite um número inteiro positivo: "))


if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:

    resultado = soma_digitos(numero)
    print("A soma dos dígitos do número é:", resultado)