#Crie um programa que receba a palavra FELICIDADE e imprima a posição de cada letra da palavra e informe qual letra está sendo impressa na posição x. 
#Após imprima a mensagem que o programa foi finalizado.

palavra = str(input("Digite uma palavra: "))

i=0
while i < len(palavra):

    print(F"Posição {i+1} da lista: {palavra[i]}")
    i+=1
