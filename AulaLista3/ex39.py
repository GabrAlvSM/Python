# Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário.

inicioInter = int(input("Digite o valor do início do intervalo: "))
fimInter = int(input("Digite o valor do fim do intervalo: "))

soma = 0
i=inicioInter
while (True):
    if ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) or (i == 2) or (i == 3) or (i==5) or (i==7)):
        soma+=i
        print("primo",i)

    elif (i==0):
        print("Fim!", soma)
        break
    i-=1


    ############ IMCOMPLETO