# Faça um algoritmo que inicialize uma lista de 10 cidades que deseja conhecer e apresente em ordem decrescente (da última para a primeira).

print("Lista de cidades por ordem alfabética:")

lista_Cidades = ["Fortaleza", "Bonito", "Rolândia", "Entrepelado", "Sombrio", "Pintópolis", "Anta Gorda", "Jijoca de Jericoacoara", "Paudalho", "Curralinhos", "Ponta Grossa"]
comprimCidad = []
cidades = {}

i=0
x=0

while (i < len(lista_Cidades)):

    while (len(cidades) < len(lista_Cidades)):
        
        if len(lista_Cidades[i]) < len(lista_Cidades[i]):
            cidades[i] = lista_Cidades[i]
        elif len(lista_Cidades[i]) >= len(lista_Cidades[i+1]):
            cidades[i] = lista_Cidades[i+1]        
        
        elif (len(cidades) == len(lista_Cidades)):

            print(cidades)

    len(lista_Cidades[i])
    # compr = len(lista_Cidades[i])
    comprimCidad.append(len(lista_Cidades[i]))
    print(comprimCidad)
    
    i+=1



# print(cidades)
# print(lista_Cidades)
# lista_Cidades.sort(key=len(compr), reverse=True)
