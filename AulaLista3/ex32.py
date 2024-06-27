# Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório 
# desses números na tela. Após exibir a soma, o programa deve mostrar também os números que 
# o usuário digitou, um por linha.

valores = []

i=0
while (len(valores) < 5):
    num = input("Digite um valor: ")

    if num == '':
        print("\nNenhum valor inserido!\n")

    else:
        num = int(num)

        valores.append(num)

soma = 0
i=0
while (i != len(valores)):
    x = valores[i]
    soma += x
    i+=1

print(f"\nSomatório dos valores: {soma} \n\nValores digitados:")

x=0
while (x < len(valores)):

    print(f"Valor {x+1}: {valores[x]}")
    x+=1