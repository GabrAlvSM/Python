# Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de 
# retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.

num = float(input("Digite um número: "))

def posinegativo(entrada):
    if entrada == 0:
        return ("Zero!")
    elif entrada > 0:
        return ("Positivo!")
    else:
        return ("Negativo!")
    

print(posinegativo(num))