class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC) -> None:
        self.ladoa = ladoA
        self.ladob = ladoB
        self.ladoc = ladoC

    def calc_perim(self):
        perimetro = self.ladoa + self.ladob + self.ladoc
        print(f"O perímetro do triângulo é: {perimetro}")

    def getMaiorLado(self):
        lados = [self.ladoa, self.ladob, self.ladoc]
        print(f"O maior lado do triângulo é: {max(lados)}")

tri1 = Triangulo(10,20,40)

tri1.calc_perim()
tri1.getMaiorLado()