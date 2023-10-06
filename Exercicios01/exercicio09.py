def filtrar(nomes):
    filtered_names = [name for name in nomes if name.startswith('A') or name.startswith('a')]
    return filtered_names

nomeList = input("Digite uma lista de nomes separados por espaços: ").split()
filtrarNomes = filtrar(nomeList)
if filtrarNomes:
    print("Nomes que começam com 'a':")
    for nome in filtrarNomes:
        print(nome)
else:
        print("Nenhum nome começando com 'a' foi encontrado na lista.")

