# Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos 
# e segundos, e os converta em segundos.

print("----")

num1 = float(input("Digite uma quantia de horas: "))
num2 = float(input("Digite uma quantia de minutos: "))
num3 = float(input("Digite uma quantia de segundos: "))

def segTransf(entrada1, entrada2, entrada3):
    entrada1 = (entrada1 * 60) * 60
    entrada2 = entrada2 * 60
    
    totalSegundos = entrada1 + entrada2 + entrada3

    return (f"\nO total de segundos é: {totalSegundos}")

print(segTransf(num1,num2,num3))