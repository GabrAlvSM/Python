# Crie um programa que leia um número inteiro positivo par N e imprima todos os números
# pares de 0 até N em ordem decrescente.

num = int(input("Digite um número par: "))

if num % 2 == 0:
    while ((num+1) != 0):
        if num % 2 == 0:
            print(num)
        num-=1

else:
    print("Apenas números pares!")