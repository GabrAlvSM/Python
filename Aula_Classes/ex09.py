class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calc_IMC(self):
        imc = self.peso / (self.altura **2)
        print(f"IMC do aluno: {imc}")

    def obter_vaor_mensalidade(self): # A academia faz um desconto especial para menores de idade,
        if self.idade < 18:
            self.mensalidade *= 0.70
            print(f"{self.mensalidade}")
        else:
            print(f"{self.mensalidade}")

incrito1 = Aluno_Academia("Paulo", 28, 80, 1.80)

incrito1.calc_IMC()
incrito1.obter_vaor_mensalidade()