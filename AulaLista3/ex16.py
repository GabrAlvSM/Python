# Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os 
# números ímpares de 1 até N em ordem crescente.

num = int(input("Digite um número ímpar: "))

if num % 2 != 0:
    i=0
    while (i < (num+1)):
        if i % 2 != 0:
            print(i)
        i += 1
else:
    print("Apenas números impares!")