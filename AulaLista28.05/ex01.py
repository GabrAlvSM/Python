# Faça um algoritmo que receba um número e apresente a tabuada do mesmo ao final.

num = int(input("Digite um número:"))

i=0
while i < (num + 1):
    print(f"{i} * {num} = {num * i}")
    i += 1