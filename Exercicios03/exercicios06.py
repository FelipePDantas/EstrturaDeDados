def conta_vogais(string):
    nome = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += nome.count(i)
    return result

solicitado = input('Informe uma palavra: ')
print(conta_vogais(solicitado))