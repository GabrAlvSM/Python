class Aluno:
    def __init__(self, nome, ra) -> None:
        self.nome = nome
        self.ra = ra
        self.notas = []

    def info_aluno(self):
        return f"Aluno: {self.nome} \nRa: {self.ra}"
    
    def mostrar_situacao(self):
        if len(self.notas) == 0:
            return f"\nO aluno {self.nome} não possui notas atribuídas!"
        else:
            media = sum(self.notas) / len(self.notas)

            if (media < 5):
                return f"\n{self.nome} - Reprovado!"
            elif (media > 5) and (media <= 6.9):
                return f"\n{self.nome} - Exame!"
            else:
                return f"\n{self.nome} - Aprovado!"
        
    def insere_notas(self):
        qnt_notas = int(input("\nInforme a quantidade de notas a serem inseridas: "))

        i=0
        while (i<qnt_notas):
            nova_nota = int(input("Insira nova nota: "))
            self.notas.append(nova_nota)
            i+=1
        
        print(f"\nForam adicionadas {len(self.notas)} notas.")

aluno1 = Aluno("Michael", 83721974)

print(aluno1.info_aluno())
print(aluno1.mostrar_situacao())

aluno1.insere_notas()

print(aluno1.mostrar_situacao())