# Um algoritmo para uma calculadora, o usuário digita o primeiro número, a operação que deseja executar e o segundo número. 
# Dependendo do que o usuário informar como operador, o algoritmo executará um cálculo diferente (soma, subtração, multiplicação ou divisão).  

num1 = float(input("\nDigite o primeiro número: "))


opcao = int(input("\nQual operação deseja realizar?\n1-Adição \n2-Subtração \n3-Multiplicação \n4-Divisão \n\n--"))

def soma():
    print("\n--- Adição ---\n")

    # num1 = int(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resp = (num1 + num2)

    print(f"\nO resultado da adição {num1} + {num2} é: {resp}\n")

def subtracao():
    print("\n--- Subtração ---\n")

    # num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resp = (num1 - num2)

    print(f"\nO resultado da subtração {num1} - {num2} é: {resp}\n")

def multi():
    print("\n--- Multiplicação ---\n")

    # num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resp = (num1 * num2)

    print(f"\nO resultado da multiplicação {num1} * {num2} é: {resp}\n")

def divis():
    print("\n--- Divisão ---\n")

    # num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 != 0 and num2 != 0:
        resp = (num1 / num2)
    
        print(f"\nO resultado da divisão {num1} / {num2} é: {resp}\n")
    else:
        print("\nOs valores não podem ser iguais a zero!\n")



if (0 < opcao < 4):

    if (opcao == 1):
        soma()
    elif (opcao == 2):
        subtracao()
    elif (opcao == 3):
        multi()
    elif (opcao == 4):
        divis()

else:
    print("Operação inválida!")
