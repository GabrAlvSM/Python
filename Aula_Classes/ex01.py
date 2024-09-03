class Pessoa:
    def __init__(self, nome, idade=0, endereco="") -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostra_info(self):
        return f"\nNome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"
    
    def altera_idade(self):
        nova_idade = input(f"\nInforme a nova idade para {self.nome}: ")
        self.idade = nova_idade
        return f"\nFoi atribuído a idade de {self.idade} para {self.nome}!"
    
    def insere_endereco(self):
        novo_endereco = input(f"\nInforme o novo endereço para {self.nome}: ")
        self.endereco = novo_endereco
        return f"Novo endereço atribuido para {self.nome}: {self.endereco}"
    
    def informa_endereco(self):
        return f"\nO endereço definido para {self.nome} é: {self.endereco}"
        

pessoa1 = Pessoa("Paulo", 23, "R. da Lagoa")

print(pessoa1.mostra_info())

pessoa2 = Pessoa("Ana")
pessoa2.altera_idade()
pessoa2.insere_endereco()
print(pessoa2.mostra_info())

print(pessoa1.informa_endereco())