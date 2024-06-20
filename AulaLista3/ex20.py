# Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser 
# informado o número de dados lidos e número de valores pares. O processo termina quando for 
# digitado o número 0.

num=1
par_cont = 0
impar_cont = 0

while (num != 0):
    num = int(input("Digite um número ou 0 para sair: "))

    if (num == 0):
        print("Fim do algorítimo!")
        break
    elif (num % 2 == 0 and num != 0):
        print("Número par!")
        par_cont+=1
    else:
        print("Número ímpar!")
        impar_cont+=1

print(f"\nQuantidade de números pares digitados: {par_cont}\nQuantidade de números ímpares digitados:{impar_cont}\n")