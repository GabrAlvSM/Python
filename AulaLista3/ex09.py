# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

lista_num = []

i=0
while (len(lista_num) != 10):

    novo_num = int(input("Digite um número: "))

    lista_num.append(int(input("Digite um número: ")))

    

print(f"Valor mínimo: {min(lista_num)} valor máximo: {max(lista_num)}")