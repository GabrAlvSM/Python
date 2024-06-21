# Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

top = max(num1,num2)
bot = min(num1,num2)

x1 = bot

soma = 0
multp = 1
while (x1 != (top+1)):
    if x1 % 2 == 0:
        soma += x1
    if x1 % 2 != 0:
        multp *= x1 
    x1+=1

print(f"\nA soma dos pares de {bot} a {top} é: {soma} \nA multiplicação dos ímpares no intervalo de {bot} a {top} é: {multp}\n")
