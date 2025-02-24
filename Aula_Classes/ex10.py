class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo=9, nivel=5) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.nivel = nivel
        self.valor = valor
        self.ligado = False
        self.consumo = consumo

    def ligar(self):
        self.ligado = True
        print("Veículo ligado!")
    
    def desligar(self):
        self.ligado = False
        print("Veículo desligado!")

    def calcImposto(self):
        imposto = self.valor * 0.025
        return imposto
    
    def abastecer(self):
        self.nivel += 70
        print("Veículo abastecido!")

    def verifNivel(self):
        return self.nivel
    
    def andar(self,km):
        litros = km / self.consumo
        self.nivel -= litros
        print("Consumo:", litros)

carr = Carro("CHEVROLET", "Celta", "Preto", 2010, 20000)
carr.ligar()
carr.desligar()

print(carr.verifNivel(), "litros")
tanque = carr.abastecer()
print(carr.nivel, "litros")

imp = carr.calcImposto()
print(f"R${imp} de imposto")

carr.andar(30)