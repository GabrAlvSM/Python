# Escreva um programa que calcule e escreva o valor de S
# S = (1/1) + (3/2) + (5/3) + (7/4) + ... (99/50)

val1 = 1
val2 = 2
s = 0

while val1 < (99+1):

    s = s + (val1/val2) 

    val1 += 2
    val2 += 1

print(s)
