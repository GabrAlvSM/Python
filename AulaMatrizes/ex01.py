# Utilizando a estruura de repetição While crie uma matriz 3x3 com os seguintes
# valores, após reescreva o código utilizando for.

# [1,2,3]
# [4,5,6]
# [7,8,9]

linhas, colunas = (3, 3)

matriz=[]

val = 1
i=0
while (i < linhas):
    linha=[]
    
    x=0
    while (x < colunas):
        linha.append(val)
        x+=1
        val+=1
    
    matriz.append(linha)
    i+=1
    
z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1


