def primo(nnumero):
    if nnumero <= 1:
        return False
    elif nnumero <= 3:
        return True
    elif nnumero % 2 == 0 or nnumero % 3 == 0:
        return False
    i = 5
    while i * i <= nnumero:
        if nnumero % i == 0 or nnumero % (i + 2) == 0:
            return False
        i += 6
    return True




numero = int(input("Digite um número para verificar se é primo: "))
if primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")

