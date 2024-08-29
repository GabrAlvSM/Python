class Pessoa: #Superclass
    def __init__(self, matricula, nome, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade

    def mostrarDados(self):
        print(self.matricula)
        print(self.nome)
        print(self.idade)
        

class Professor(Pessoa): #Subclass
    def __init__(self, matricula, nome, idade, formacao, disciplina, ch, salario):
        super().__init__(matricula,nome,idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.ch = ch
        self.salario = salario
        
    def mostrarDados(self):
        print(self.matricula)
        print(self.nome)
        print(self.idade)
        print(self.salario)

    def lecionar(self):
        print(f"{self.nome} está lecionando!")

class Aluno(Pessoa): #Subclass
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas

    def calc_media(self):
        media = sum(self.notas) / len(self.notas)
        if media < 7.0:
            return f"{self.nome} - Reprovado!"
        elif 5.0 < media <= 6.9:
            return f"{self.nome} - Exame!"
        else:
            return f"{self.nome} - Aprovado!"


# pessoa1 = Pessoa(1001, "Gabriel", 25)
# pessoa1.mostrarDados()

pessoa2 = Professor(200, "Thiago", 28, "Analise de Sistemas", "Algoritimos", 40, 10000)
pessoa2.mostrarDados()
pessoa2.lecionar()

aluno1 = Aluno(1002, "Paulo", 20, [7,8,7.5,10])
nota = aluno1.calc_media()
print(nota)