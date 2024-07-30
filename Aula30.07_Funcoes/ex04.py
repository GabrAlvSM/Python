# 4 – Escreva um programa, com uma função que necessite de um argumento. A função retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def argumento(val):

    if (val > 0):
        return "Positivo"
    elif (val == 0):
        return "Zero!"
    else:
        return "Negativo!"

res = argumento(int(input("Digite um número: ")))

print(res)