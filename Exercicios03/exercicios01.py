soma_notas =0

for i in range(1, 6):
    nota = float(input(f"Digite a {i} nota: "))
    soma_notas += nota

media = soma_notas / 5

if media >= 7:
    print(f"Média: {media:.2f}")
    print("Aprovado")
else:
    print(f"Média: {media:.2f}")
    print("Reprovado")