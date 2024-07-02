# Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos 
# pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
# entre com um valor para resistência igual a zero

# R = ((r1 * r2) / (r1 + r2))

while (True):
    res1 = int(input("\nDigite o valor da primeira resistência: "))
    res2 = int(input("Digite o valor da segunda resistência: "))
    
    if (res1 == 0 or res2 == 0):
        print("\nfim do algorítimo!\n")
        break

    else:
        resTotal = (res1 * res2) / (res1 + res2)
        print (f"\nResistência da associção: {resTotal:.3f}")