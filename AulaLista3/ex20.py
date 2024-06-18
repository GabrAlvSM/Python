# Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser 
# informado o número de dados lidos e número de valores pares. O processo termina quando for 
# digitado o número 0.

num=1

while (num != 0):
    num = int(input("Digite um número: "))

    if (num == 0):
        print("Fim do algorítimo!")
        break
    elif (num % 2 == 0 and num != 0):
        print("Número par!")
    else:
        print("Número ímpar!")