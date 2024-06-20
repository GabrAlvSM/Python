# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse 
# número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
#     1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

num = int(input("Digite um número: "))
divisores = []

i=1
soma = 0
while (i < num):
    if (num % i == 0):
        divisores.append(i)
        soma += i

    i+=1

print("A soma dos divisores do número {} é: {} = {}".format(num, divisores, soma))