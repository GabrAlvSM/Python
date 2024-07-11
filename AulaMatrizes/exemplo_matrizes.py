linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))

matriz=[]

i=0
while (i < linhas):
    linha=[]

    x=0
    while (x < colunas):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
        x+=1
    
    matriz.append(linha)
    i+=1
    

z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1


