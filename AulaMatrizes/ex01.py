# Utilizando a estruura de repetição While crie uma matriz 3x3 com os seguintes
# valores, após reescreva o código utilizando for.

# [1,2,3]
# [4,5,6]
# [7,8,9]

linhasY, colunasX = (3, 3) # Tamanho da matriz

matriz=[]

val = 1
i=0
while (i < linhasY):
    linha=[]
    
    x=0
    while (len(linha)<linhasY):
        linha.append(val)
        x+=1
        val+=1
    
    matriz.append(linha)
    i+=1
    
z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1