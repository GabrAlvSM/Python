qnt350 = int(input("Digite a quantidade de latas adquiridas: "))
qnt600 = int(input("Digite a quantidade de garrafas de 600ml adquiridas: "))
qnt2L = int(input("Digite a quantidade de garrafas de 2L adquiridas: "))

total = ((qnt350 * 350) + (qnt600 * 600) + (qnt2L * 2000)) / 1000

print(f"A quantidade total de litros comprados foi de {total} litros.")