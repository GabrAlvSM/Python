class Nota_fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, val_prods, icms, frete, ipi, val_total) -> None:
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.raz_soc = razao_social
        self.data = data
        self.val_prods =val_prods
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.val_total = val_total

