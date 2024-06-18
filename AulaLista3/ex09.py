# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

lista_num = []

i=0
while (len(lista_num) < 10):

    lista_num.append(int(input("Digite um número: ")))

print(f"Menor valor inserido: {min(lista_num)}. Maior valor lido: {max(lista_num)}")