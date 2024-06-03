# Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa 
# (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. Ex: Bife acebolado R$15,00; Lasanha R$25,00). 
# A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário, 
# “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), 
# caso contrário, mostrar o valor final (somente o valor do prato). 

cardapio = ("Bife acebolado ", "Lasanha ", "Bife à parmegiana", "Coca Cola ", "Suco de acerola")
valores = (20.0, 15.0, 20.0, 4.50, 6.0)

i=0
while (i < len(cardapio)):
    print(f"{i+1} {cardapio[i]} R$ {valores[i]}")
    i = i + 1

opcao = int(input("\nDigite o número do item desejado: "))
opcao = opcao - 1

extra = input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato? S/N \n\n--")

if extra == 'S':
    total = valores[opcao] * 1.1
    print(f"Valor final da compra: {total}")

else:
    print(f"Valor final da compra: {valores[opcao]}")
