class Aluno:
	def __init__(self,nome,turma=32):
		self.nome = nome
		self.turma = f'Fábrica {turma}'

	def study(self,lista):
		print(f" {self.nome} Estudando Python no Linux ...ex: ", lista)

aluno = Aluno("Thiago")
aluno.study([58,59,60,159])
