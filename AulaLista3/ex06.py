# Escreva um programa que peça ao usuário para digitar 10 valores e some-os.

i=0
soma = 0
while i != 10:
    novo_num = int(input("Digite um número: "))
    soma = novo_num + soma
    i+=1

print(soma)
