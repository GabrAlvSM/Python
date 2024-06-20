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
            print(f"idades já contabilizadas: \n{idades_lista}")
        
soma = 0
i=0
while (i != len(idades_lista)):
    x = idades_lista[i]
    soma += x
    i+=1

media = soma / len(idades_lista)

print(f"A média de idade é: {media}\n")