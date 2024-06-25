# Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando 
# for informada a idade 0), e calcule a idade média desse grupo.

idades_lista = []

while (True):
    idade = (input("Digite sua idade: "))

    if idade == '':
        print("\nNenhum valor inserido!\n")
    
    else:
        idade = int(idade)
        if idade == 0:
            print(f"\n{len(idades_lista)} valores adicionados.\n")
            break
        
        else:

            idades_lista.append(idade)
            print("idades já contabilizadas: ", end=" ")

            x=0
            while (x < len(idades_lista)):

                if (x == len(idades_lista)-1):
                    print(idades_lista[x], end=".")
                else:
                    print(idades_lista[x], end=", ")
                x+=1
            print("\n")
        
soma = 0
i=0
while (i != len(idades_lista)):
    x = idades_lista[i]
    soma += x
    i+=1

media = soma / len(idades_lista)

print(f"A média de idade é: {round(media,2)}\n")