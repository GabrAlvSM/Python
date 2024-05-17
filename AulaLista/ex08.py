from datetime import date


ano = date.today().year

idade = int(input("Digite sua idade: "))

nasc = ano - idade

print("Seu ano de nascimento é: ", nasc)