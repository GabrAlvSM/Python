# Faça um algoritmo que receba 10 nomes em uma lista, e ao final apresente todos os nomes recebidos.

lista_nomes = []
i=0

while i < 10 :

    nome_nov = input("Digite o um nome: ")
    lista_nomes.append(nome_nov)
    i+=1    
    
    if len(lista_nomes) == 10:

        lista_nomes.sort()

        print("Lista de nomes: \n")

        for nomes in lista_nomes:
            print(nomes)