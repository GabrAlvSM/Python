class Circulo:
    def __init__(self,raio) -> None:
        self.raio = raio
    
    def imprime_raio(self):
        return f"Raio do círculo: {self.raio}"
    
    def calc_area(self):
        area = (self.raio * 3.14)**2
        return f"Area do círculo: {area}"
    
    def calc_circunf(self):
        print (f"Circunferência do círculo: {(2 * 3.14 * self.raio)}")
    
circ1 = Circulo(5)

print(circ1.imprime_raio())
print(circ1.calc_area())
circ1.calc_circunf()