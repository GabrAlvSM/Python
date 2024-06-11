# Escreva um programa que leia 10 inteiros e imprima sua média.

media = 0
for num in range(1,11):
    novo_num = int(input("Digite um número: "))
    media = novo_num + media

media = media/10
print(media)