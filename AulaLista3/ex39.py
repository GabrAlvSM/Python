# Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário.

inicioInter = int(input("Digite o valor do início do intervalo: "))
fimInter = int(input("Digite o valor do fim do intervalo: "))

interv = fimInter - inicioInter

i = inicioInter
root_i = i**(1/2)

contador = 0
if (inicioInter >= 0 and interv >= 0):

    while (interv > 0):
                
        if (i % 2 != 0 and i > 1):
            x=1
            while(x < root_i):
                if (i % x != 0):
                    print("primo!", i)
                    contador+=1
                    break
                x+=2
                
            # if (x >= root_i):
                # print("não primo", i)
                # interv-=1
              
        elif (i % 2 != 0 or i == 2 or i == 3):
            print("primo!", i)
            contador+=1
        
        # else:
        #     print("primo!", i)
            
        interv-=1
        i+=1


else:
    print("O início do intervalo deve ser positivo e o valor do final do intervalo deve ser maior que inicial!")

print(f"Quantidade de primos no intervalo de {inicioInter} a {fimInter}: {contador}")



    # while (True):
    #     if ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) or (i == 2) or (i == 3) or (i==5) or (i==7)):
    #         contador+=1
    #         print("primo",i)

    #     elif (interv==0):
    #         print("Fim!", contador)
    #         break
        
    #     interv-=1
    #     i+=1
    ########