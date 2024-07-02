# Chico tem 1.70 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.20 metros e cresce 3 
# centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão
# necessários para que Zé seja maior que Chico.

altChico = 1.50
altZe = 1.40

anos = 1 

while (altZe <= altChico):
    altChico = altChico + 0.02
    altZe = altZe + 0.03

    print(f"Após {anos} anos:")
    print(f"Chico: {altChico:.2f} M")
    print(f"Zé: {altZe:.2f} M\n")

    anos+=1

print(f"Após {anos-1} anos Zé será maior que Chico")