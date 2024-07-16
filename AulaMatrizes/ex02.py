# Utilizando a estrutura de repetição While crie um programa que inicialize uma matriz 4 x 4, o usuário deve digitar os dados de entrada de cada elemento da matriz. Durante a execução o programa deve informar qual linha e coluna o usuário está preenchendo. 
# Ao final imprima a matriz preenchida pelo usuário. 
#
# Entrada: dados
#
# Saída: 
# ['12','11','10','32']
# ['40','50','44','10']
# ['99','12','15','16']
# ['18','19','20','22']


linhasY, colunasX = (4, 4) # Tamanho da matriz

matriz=[]


i=0
while (i < linhasY):
    linha=[]
    
    x=0
    while (len(linha)<linhasY):
        val = int(input(f"Digite um valor para ser adicionado á posição [{i},{x}]:"))
        linha.append(val)
        x+=1
    
    matriz.append(linha)
    i+=1
    
z=0
while (z<len(matriz)):
    print(matriz[z])
    z+=1