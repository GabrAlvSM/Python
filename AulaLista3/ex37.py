# Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número
# fornecido é primo ou não.

num = int(input("Digite um número: "))

if (num % 2 != 0 and num % 3 != 0 or num == 2 or num == 3):
    print("primo!")
else:
    print("não primo!")