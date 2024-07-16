# Faça um programa que leia uma matriz de 3 x 3 elementos, multiplique cada elemento de cada linha por 5 e armazene a multiplicação em uma nova matriz. Exemplo:

# entrada: [1,2,3]
#          [4,5,6]
#          [7,8,9]


matriz = [[1,2,3],[4,5,6],[7,8,9]]
nova_matriz=[]

linhasY, colunasX = (3, 3) # Tamanho da matriz


i=0
while (i < linhasY):
    linha=[]
    
    x=0
    while (len(linha)<linhasY):
        val = matriz[i][x] *5 ## [i] = lista dentro da lista 'matriz', [x] = valor dentro da lista 'i' da 'matriz'
        
        linha.append(val)
        x+=1
    
    nova_matriz.append(linha)
    i+=1
    

print("Matriz de entrada: ")
z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1

print("\n")

print("Matriz de saída: ")
z=0
while (z<len(nova_matriz)):
    print(nova_matriz[z])
    z+=1