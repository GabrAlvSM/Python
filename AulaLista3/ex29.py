# Crie um programa que calcule o menor número divisível por cada um dos números de 1 a 20? 
# Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem 
# sobrar resto

num = int(input("Digite um valor: "))
divisiveis = []

i=1
while (i<21):
    if num % i == 0:
        divisiveis.append(i)
    i+=1

print(f"O número {num} é divisível por: ", end=" ")


#IMPRIME OS VALORES EM UMA MESMA LINHA, SEPARADOS POR VÍRGULA E COM PONTO FINAL
x=0
while (x < len(divisiveis)):

    if (x == len(divisiveis)-1):
        print(divisiveis[x], end=".")
    else:
        print(divisiveis[x], end=", ")
    x+=1