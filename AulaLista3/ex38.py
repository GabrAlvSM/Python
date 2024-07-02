# Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros 
# números primos.

num = int(input("Digite um número: "))

soma = 0
i=num
while (True):
    if ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) or (i == 2) or (i == 3) or (i==5) or (i==7)):
        soma+=i
        print("primo",i)

    elif (i==0):
        print("Fim!", soma)
        break
    i-=1