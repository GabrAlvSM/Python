# Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário.

inicioInter = int(input("Digite o valor do início do intervalo: "))
fimInter = int(input("Digite o valor do fim do intervalo: "))

soma = 0
interv = fimInter - inicioInter

i = inicioInter
root_i = i**(1/2)


if (inicioInter >= 0 and fimInter > inicioInter):
    # while (True):
    #     if ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) or (i == 2) or (i == 3) or (i==5) or (i==7)):
    #         soma+=1
    #         print("primo",i)

    #     elif (interv==0):
    #         print("Fim!", soma)
    #         break
        
    #     interv-=1
    #     i+=1
    ########

    while (interv > 0):
                
        if (i % 2 != 0 and i > 3):
            x=3
            while(x < root_i):
                if (i % x == 0):
                    print("não primo!", i)
                    break
                x+=1
                if (i >= root_i):
                    print("primo", i)
                    soma+=1
                    break
                
        
        elif (i % 2 == 0 and i != 2):
            print("não primo!", i)
            

        else:
            print("primo!", i)
            soma+=1
            
    
        interv-=1
        i+=1


else:
    print("O início do intervalo deve ser positivo e o valor do final do intervalo deve ser maior que inicial!")

print("yo yo yo yooo",soma)