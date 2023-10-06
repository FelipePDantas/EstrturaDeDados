entrada = input("Digite uma lista de números separados por espaços: ")

numeros_em_texto = entrada.split()

numeros = [int(numero) for numero in numeros_em_texto]

soma = 0
pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma+= numero
        pares += 1

# Calcula a média dos números pares
if pares > 0:
    media= soma / pares
    print(f"A média dos números pares na lista é: {media}")
else:
    print("Não foram encontrados números pares na lista.")