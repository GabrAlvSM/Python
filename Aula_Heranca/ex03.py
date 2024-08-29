class Ingresso:
    def __init__(self, preco, setor) -> None:
        self.preco = preco
        self.setor = setor

    def alterarPreco(self, novoPreco):
        self.preco = novoPreco

    def mostrarSetor(self):
        return self.setor
    
class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento) -> None:
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegarBebida(self):
        if self.open_bar:
            return "Bebida liberada!"
        else:
            return "Compre fichas no caixa!"

    def acessarCamarote(self):
        if self.camarote:
            return "Acesso liberado"
        else:
            return "Acesso não liberado ao camarote!"


acdc = Ingresso(200, "VIP")

acdc.mostrarSetor()
print(acdc.preco)
acdc.alterarPreco(250)
print(acdc.preco)
        
opcao1 = IngressoVIP(200, "VIP", True, True, False, False)
pinga = opcao1.pegarBebida()
print(pinga)