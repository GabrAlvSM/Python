## Classe Pessoa
#Abstração do objeto pessoa na programação orientada a objetos

## Atribuos - nome,idade,email,cidade,estado
# Métodos - comer,dormir, estudar (Ações -> Funções -> Métodos)

class Pessoa:
    # SEMPRE INICICAR PELO MÉTODO CONSTRUTOR
    def __init__(self,nome,idade,email,cidade): # Construtor
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cidade = cidade

    # TODOOS OS MÉTODOS DEVEM TER COMO PARAMETRO SELF
    def hello(self): # MÉTODO 
        print(f'Hello {self.nome}')

## Instanciar uma classe
        
pes1 = Pessoa("Alvin", 18, "alvin@email.com", "Campo Grande")
# print(pes1.nome)
# print(pes1.idade)

pes2 = Pessoa("Maria", 52, "maria@email.com", "Rio de Janeiro")
# print(pes2.nome)
# print(pes2.idade)

pes2.hello()