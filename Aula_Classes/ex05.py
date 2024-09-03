class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.hr_trab = horas_trabalhadas
        self.val_hora = valor_hora

    def insere_nome_compl(self):
        self.nome = input("Informe o nome do funcionário: ")
        self.sobrenome = input("Informe o sobrenome do funcionário: ")
        print(f"Nome completo do funcionário: {self.nome} {self.sobrenome}")

    def calc_salario(self):
        self.hr_trab = float(input(""))
        