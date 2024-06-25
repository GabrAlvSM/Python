# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número
# negativo. O programa tem que retornar o maior e o menor número lido.

valores = []

i=0
while (True):
    num = input("Digite um valor: ")

    if num == '':
        print("\nNenhum valor inserido!\n")

    else:
        num = int(num)
        if num >= 0:
            valores.append(num)
        else:
            break

print(f"\nValor mínimo digitado: {min(valores)} \nValor máximo digitado:{max(valores)}")