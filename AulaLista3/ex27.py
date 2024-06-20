# Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do 
# Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

num = int(input("Digite um número: "))
fatorial = []

i=num
total = num
while True:
    if (i > 1):
        total = total * (i -1)
        fatorial.append(i)
    elif (i == 1):
        fatorial.append(i)
        break
    i-=1

print("O fatorial de {} é: {} = {}".format(num, fatorial, total))