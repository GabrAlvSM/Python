# Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros 
# números naturais.

num = int(input("Digite um número: "))
if num > -1:
    
    i = 0
    soma = 0
    while i < (num+1):
        soma = soma + i
        i+=1
    print(f"A soma dos números primeiros {num} números naturais é: {soma}")

else:
    print("Apenas números positivos!")