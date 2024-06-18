# Crie um programa que leia um número inteiro N e depois imprima os N primeiros números
# naturais ímpares

num = int(input("Digite um número: "))

i=0
while (i < num):
    i = i + 1
    if i % 2 != 0:
        print(i)