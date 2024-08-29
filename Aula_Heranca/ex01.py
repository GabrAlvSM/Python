class Filme:
    def __init__(self, nome, duracao) -> None:
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print("Filme iniciado!")

    def pause(self):
        print("Filme pausado!")

class Acao(Filme):
    def __init__(self, nome, duracao) -> None:
        super().__init__(nome, duracao)
    
    def explodir(self):
        print("BOOOOM")

class Drama(Filme):
    def __init__(self, nome, duracao) -> None:
        super().__init__(nome, duracao)

    def matar(self):
        print("O autor matou o seu personagem favorito!")

class Suspense(Filme):
    def __init__(self, nome, duracao) -> None:
        super().__init__(nome, duracao)

    def tencao(self):
        print("~~musica tensa~~")