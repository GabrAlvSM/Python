# Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
# média.

lista_num = []

i=0
while (len(lista_num) != 10):
    novo_num = int(input("Digite um número: "))

    if novo_num >= 0:
        lista_num.append(novo_num)
        i+=1
    else:
        print("Apenas números positivos!")
    
n=0
soma = 0
for i in lista_num:
    soma = lista_num[1] + soma
soma = soma / 10
print(soma)