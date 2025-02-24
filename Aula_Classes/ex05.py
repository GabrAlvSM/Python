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
        if (self.hr_trab is None or self.hr_trab == ''):
            self.hr_trab = float(input("\nInforme a quantidade de horas trabalhadas: "))
        if (self.val_hora is None or self.val_hora == ''):
            self.val_hora = float(input("\nInforme o valor da hora de serviço do funcionário: "))
        # multiplicando o atributo horasTrabalhadas pelo atributo valorPorHora
        sal_mes = self.val_hora * self.hr_trab
        print(f"\nO funcionário {self.nome} deve receber {sal_mes} por suas {self.hr_trab} horas trabalhadas.")

    def incrementar_horas(self):
        adicionahora = float(input(f"\nInforme a quantidade de horas a serem adicionadas para o funcionário {self.nome} {self.sobrenome}: "))
        self.hr_trab += adicionahora
        print (f"\nForam adicionadas {adicionahora} horas ao quadro do funcionário {self.nome} {self.sobrenome}, totalizando {self.hr_trab} horas trabalhadas.")

    def info_funcionario(self):
        return f"\nNome: {self.sobrenome}, {self.nome} \nHoras trabalhadas: {self.hr_trab} \nValor por hora de serviço: {self.val_hora}"
    
john = Funcionario("John", "", 40, 30)

print(john.info_funcionario())
john.insere_nome_compl()
john.calc_salario()
john.incrementar_horas()
john.calc_salario()