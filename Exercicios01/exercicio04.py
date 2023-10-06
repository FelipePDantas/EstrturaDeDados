entrada = input("Digite uma lista de números separados por espaços: ")

numeros_em_texto = entrada.split()


numeros = [int(numero) for numero in numeros_em_texto]


if len(numeros) == 0:
    print("A lista está vazia. Não há valores para encontrar o maior e o menor.")
else:

    maior = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    print(f"O maior valor na lista é: {maior}")
    print(f"O menor valor na lista é: {menor}")