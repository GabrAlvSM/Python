# Faça um algoritmo que inicialize uma lista de 10 cidades que deseja conhecer e apresente em ordem decrescente (da última para a primeira).

print("Lista de cidades por ordem alfabética:")

lista_Cidades = ["Fortaleza", "Bonito", "Rolândia", "Entrepelado", "Sombrio", "Pintópolis", "Anta Gorda", "Jijoca de Jericoacoara", "Paudalho", "Curralinhos", "Ponta Grossa"]
lista_Cidades.sort()

i=0
while (i < len(lista_Cidades)):
    print(lista_Cidades[i])
    i+=1