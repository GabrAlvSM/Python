class Conta:
    def __init__(self, nome, cpf, saldo=0) -> None:
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self):
        deposito = float(input("\nInforme o valor do depósito: "))
        self.saldo += deposito
        print(f"Saldo em conta atual: {self.saldo}")
    
    def sacar(self):
        saque = float(input("\nInforme o valor do saque: "))
        if ((self.saldo - saque) < 0):
            print("Saldo insuficiente para saque!")
            return
        else:
            self.saldo -= saque
            print(f"Saldo em conta atual: {self.saldo}")
    
    def impr_saldo(self):
        print(f"\nSaldo em conta atual: {self.saldo}")
    
    def info_conta(self):
        print(f"\nNome: {self.nome} \nCPF: {self.cpf} \nSaldo Disponível: {self.saldo}")
    
conta1 = Conta("Ann", "123.456.789-00", 10000.00)

print(conta1.info_conta())
conta1.depositar()
conta1.sacar()
conta1.impr_saldo()

