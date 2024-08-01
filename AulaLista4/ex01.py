# Crie uma função que receba dois números como parâmetros e mostre a potência do número elevado a n vezes, exemplo: 
# pot(2,3)
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8

def whatever(val1,val2):
    i=1
    while (i < val2+1):
        x = val1 ** (i)
        print (f"{val1} ^ {i} = {x}")
        i+=1

base = float(input("Digite um número: "))
expt = float(input("Digite uma potência máxima: "))
    
whatever(base,expt)