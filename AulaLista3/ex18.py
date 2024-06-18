# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A 
# quantidade de números a serem lidos deve será fornecida pelo usuário.

lista_num = []

print("Digite 5 números: ")

i=0
while (len(lista_num) < 5):

    lista_num.append(int(input("Digite um número: ")))

print(f"Maior valor lido: {max(lista_num)}")