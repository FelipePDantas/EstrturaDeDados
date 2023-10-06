class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"



titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")

livro = Livro(titulo, autor)

print("\nDetalhes do Livro:")
print(livro.detalhes())