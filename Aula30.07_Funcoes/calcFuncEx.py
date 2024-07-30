def potenc(x,y):
    res = x ** y
    return res

def soma(x,y):
    res = x + y
    return res

def multipl(x,y):
    res = x * y
    return res


print("--Calculadora--")

escolha = int(input("1-Soma\n2-Multiplicação\n3-Exponenciação\n\n-- "))

if (escolha == 1): #soma
    val1 = int(input("Digite o primeiro valor: ")) 
    val2 = int(input("Digite o segundo valor: "))

    x = soma(val1,val2)

elif (escolha == 2): #multiplicação
    val1 = int(input("Digite o primeiro valor: ")) 
    val2 = int(input("Digite o segundo valor: "))

    x = multipl(val1,val2)

elif (escolha == 3): #exponenciacao
    val1 = int(input("Digite a base: "))
    val2 = int(input("Digite o expoente: "))

    x = potenc(val1,val2)

else:
    print("Apenas de 1 a 3!")
    

print(f"Resultado: {x}")