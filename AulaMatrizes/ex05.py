# Crie um programa que inicialize uma matriz 8 x 8 no formato de uma rifa, preenchida com números 1. 
# Em seguida solicite ao usuário a entrada da linha e coluna que deseja marcar um X e imprima novamente a matriz com a alteração realizada. 
# Neste exercício estamos simulando a escolha de uma posição em uma rifa, caso necessário, você pode alimentar a rifa com números em sequência.

linhasY, colunasX = (8, 8) # Tamanho da matriz

matriz = []

val = 1
i=0
while (i < linhasY):
    linha=[]
    
    x=0
    while (len(linha)<linhasY):
        linha.append(val)
        x+=1
    
    matriz.append(linha)
    i+=1

print("Rifa: ")
z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1


while(True):
    escolhaX = int(input("Digite a linha (1 a 8): ")) - 1
    escolhaY = int(input("Digite a coluna (1 a 8): ")) - 1

    if ((0 <= escolhaX <= 7) and (0 <= escolhaY <= 7)):

        matriz[escolhaX][escolhaY] = "X"
        break
    else:
        print("Os valores devem estar dentro dos limites da rifa!")

print("Rifa marcada: ")
z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1
