# Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os 
# números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores.

valores = []
pares = []
impares = []

i=0
while (len(valores) < 20):
    num = input(f"[{i+1}]Digite um valor: ")
   
    if (num == '' or num == '0'):
        print("\nNenhum valor inserido!\n")

    else:
        num = int(num)
        if (num % 2 == 0): # par
            pares.append(num)
            valores.append(num)
       
        elif (num % 2 != 0): # impar
            impares.append(num)
            valores.append(num)
        i+=1

# lista completa
print ("valores:", end=" ")
x=0
while (True): 

    if (x == len(valores)-1):
        print(valores[x], end=".\n")
        break
    else:
        print(valores[x], end=", ")
    x+=1

# lista de pares
print ("pares: ", end=" ")
x=0
while (True): 

    if (x == len(pares)-1):
        print(pares[x], end=".\n")
        break
    else:
        print(pares[x], end=", ")
    x+=1

# lista de impares
print ("impar:", end=" ")
x=0
while (True): 

    if (x == len(impares)-1):
        print(impares[x], end=".\n")
        break
    else:
        print(impares[x], end=", ")
    x+=1
