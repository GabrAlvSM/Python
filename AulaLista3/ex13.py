# Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais 
# de 0 até N em ordem decrescente.

num = int(input("Digite um número: "))

while ((num+1) != 0):
    print(num)
    num-=1