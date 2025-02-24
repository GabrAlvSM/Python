class Agenda:
    def __init__(self, dia, mes, ano, anotacao) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        if self.dia is None or self.dia == '' :
            self.dia = int(input("Informe o dia atual: "))
        if self.mes is None or self.mes == '':
            self.mes = int(input("Informe o mês atual: "))
        if self.ano is None or self.ano == '':
            self.ano = int(input("Informe o ano atual: "))
        return f"{self.dia}/{self.mes}/{self.ano}"
    
    def anotar_tarefa(self):
        if self.dia is None or self.mes is None or self.ano is None:
            print("É necessário que a data esteja devidamente preenchida!")
        else:
            self.anotacao = input(f"\n{self.dia}/{self.mes}/{self.ano}\nAnotação: ")
            print(self.anotacao)

    def mostrar_anotacao(self):
        if self.anotacao is None or self.anotacao == '' :
            print( f"Sem anotações para a data {self.dia}/{self.mes}/{self.ano}")
        else:
            print(self.anotacao)
        
date1 = Agenda(None, None, None, None)

date1.validar_data()
date1.mostrar_anotacao()
date1.anotar_tarefa()
date1.mostrar_anotacao()