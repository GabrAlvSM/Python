# 1 - Crie uma função que necessite de três argumentos, e que imprima o produto desses três argumentos.

def trinity(x:int,y:int,z:int):
    res = (x + y) * z
    return res

print("Função: (x + y) * z")

var1 = int(input("Digite o valor de x: "))
var2 = int(input("Digite o valor de y: "))
var3 = int(input("Digite o valor z: "))

print("Resposta: ",trinity(var1,var2,var3))