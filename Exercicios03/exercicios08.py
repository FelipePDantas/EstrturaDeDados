def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


opcao = int(input("Digite 1 para  converter de Celsius para Fahrenheit e 2 para o contrario: "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius equivalem a {resultado:.2f} graus Fahrenheit.")
else:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit equivalem a {resultado:.2f} graus Celsius.")