class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)


nomeAluno = input("Digite o nome do aluno: ")
notasAluno = []

while True:
    nota = float(input("Digite uma nota (ou digite -1 para encerrar): "))
    if nota == -1:
        break
    notasAluno.append(nota)

aluno = Aluno(nomeAluno, notasAluno)
media = aluno.calcular_media()
print(f"A média das notas do(a) aluno(a) {aluno.nome} é {media:.2f}")