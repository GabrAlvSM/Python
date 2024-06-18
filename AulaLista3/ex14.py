# Crie um programa que leia um número inteiro positivo par N e imprima todos os números 
# pares de 0 até N em ordem crescente.

num = int(input("Digite um número par: "))

if num % 2 == 0:
    i=0
    while (i < (num+1)):
        if i % 2 == 0:
            print(i)
        i += 1
else:
    print("Apenas números pares!")