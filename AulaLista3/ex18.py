# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A 
# quantidade de números a serem lidos deve será fornecida pelo usuário.

qnt = int(input("Informe a quantidade de valore a serem lidos: "))
lista_num = []

print(f"\nDigite {qnt} números: ")

i=0
while (len(lista_num) < qnt):

    lista_num.append(int(input("Digite um número: ")))

print(f"Maior valor lido: {max(lista_num)}")