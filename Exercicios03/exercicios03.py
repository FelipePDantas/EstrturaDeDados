frase = str.upper(input('Digite uma frase: ')).strip()
fraseLimpa = str.replace(frase, ' ','')
if fraseLimpa == fraseLimpa[::-1]:
    print('é palíndromo')
else:
    print('não é palíndromo')