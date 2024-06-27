# Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida 
# receba um novo valor do usuário e verifique se este valor se encontra no vetor

vetor = []

i=0
while (len(vetor) < 10):
    num = input(f"[{i+1}]Digite um valor: ")
   
    if num == '':
        print("\nNenhum valor inserido!\n")

    else:
        num = int(num)

        vetor.append(num)
        i+=1


# mostra os valores adicionados
print("Valores contabilizadas: ", end=" ")

x=0
while (x < len(vetor)):

    if (x == len(vetor)-1):
        print(vetor[x], end=".")
    else:
        print(vetor[x], end=", ")
    x+=1

# compara se o valor já foi digitado
num = int(input("\n\nDigite um valor: "))

i=0
while (True):
    if i == len(vetor):
        print("O valor não se encontra na lista!")
        break
    
    if num == vetor[i]:
        print("O valor se encontra na lista!")
        break

    i+=1
