def sequencia_fibonacci(n):
    sequencia = [0, 1]
    for i in range(2, n + 1):
        proximo_numero = sequencia[i - 1] + sequencia[i - 2]

        if proximo_numero <= n:
            sequencia.append(proximo_numero)
        else:
            break
    return sequencia


valor_maximo = int(input("Digite o valor máximo para a sequência de Fibonacci: "))
sequencia_fib = sequencia_fibonacci(valor_maximo)
print("Sequência de Fibonacci até", valor_maximo, ":", sequencia_fib)