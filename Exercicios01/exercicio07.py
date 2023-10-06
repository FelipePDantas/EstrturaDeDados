def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Inicializamos com os dois primeiros números da sequência
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence




n = int(input("Digite um valor máximo para a sequência de Fibonacci: "))
if n < 0:
     print("Por favor, insira um valor positivo.")
else:
    result = fibonacci_sequence(n)
    print("Sequência de Fibonacci até", n, ":")
    print(result)

