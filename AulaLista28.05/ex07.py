# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

num = int(input("Digite um número:"))

if num > 0:

    i=0
    while (i < num):

        num = num + 1
        if num % 2 != 0:
            print(num)
