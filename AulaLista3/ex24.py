# Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 
# ou 5.

i=0
soma = 0
while (i != 1000):
    if ((i % 3 == 0) or (i % 5 ==0)):
        soma += i

    i+=1

print(soma)