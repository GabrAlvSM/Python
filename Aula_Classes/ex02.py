class Livro:
    def __init__(self, nome, autor, editora, paginas=0) -> None:
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self):
        nova_editora = input(f"\nInforme nova editora para o livro {self.nome}: ")
        self.editora = nova_editora
        return f"Nova editora atribuída: {self.editora}"
    
    def info_livro(self):
        return f"Livro: {self.nome} \nAutor: {self.autor} \nEditora: {self.editora} \nQnt. páginas: {self.paginas}"


livro1 = Livro("Clean Code", "Robert Cecil Martin", "Pearson", 402)

print(livro1.info_livro())

livro1.alterar_editora()

print(livro1.info_livro())
