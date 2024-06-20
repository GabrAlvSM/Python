#  Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um 
# dos algarismos que compõem o número.

num = int(input("Digite um número de 100 a 9999: "))

if (100 <= num <= 9999):
    num = str(num)

    i=0
    while i < len(num):

        print(F"Posição {i+1} da lista: {num[i]}")
        i+=1
else:
    print("Apenas valores de 100 a 9999!!")
