

inicioInter = int(input("Digite o inicio do intervalo: "))
finalInter = int(input("Digite o final do intervalo: "))

if inicioInter > finalInter:
    print("O valor inicial deve ser menor!")

else:
    soma=0
    while (inicioInter <= finalInter):
        if inicioInter % 2 == 0:
            inicioInter+=1
        else:
            print(inicioInter)
            soma += inicioInter
            inicioInter+=2

    print(soma)