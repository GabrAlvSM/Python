# Crie um programa que leia uma lista de 9 posições e converta em uma matriz de 3x3:

numeros = [10,20,30,100,200,300,1000,2000,3000]
matriz = []

linhasY, colunasX = (3, 3) # Tamanho da matriz

ex=0
i=0
while (i < linhasY):
    linha=[]
    
    x=0 + ex
    while (len(linha)<linhasY):
        
        val = numeros[x]
        linha.append(val)
        x+=1
    
    matriz.append(linha)
    i+=1
    ex+=3

z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1