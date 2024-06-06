# Validar CPF
#     O cálculo do CPF é baseado nos 2 dígitos finais.
#     Para validar, pegue os nove primeiros dígitos do CPF, gere os dois
#     dígitos e salve em um novo CPF.
#     Compare se o CPF enviado é igual ao CPF gerado.
#     Se verdadeiro, o CPF é válido, caso contrário, inválido.

# * Obter primeiro dígito:
#     1 - Multiplicar os 9 primeiros dígitos do CPF por uma contagem
#         regressiva iniciando de 10 e terminando em 2
#     2 - Somar todos os valores das multiplicações do passo 1
#     3 - Obter o resto da divisão entre a soma e 11 do passo 2
#     4 - Subtrair o resultado do passo 3 por 11
#     5 - Se o resultado do passo 4 for maior que nove, o dígito é zero,
#         caso contrário, o dígito é o valor do passo 4

# * Obter segundo dígito:
#     1 - Multiplicar os 10 primeiros dígitos do CPF, por uma contagem 
#         contagem regressiva iniciando de 11 e terminando em 2
#     2 - Mesma lógica do passo 2 do primeiro dígito em diante.

# Observações:
#     Tomar cuidado com sequência de caracteres,
#     elas podem gerar CPFs válidos.


cpfInput = input("\nDigite seu CPF: ")
cpfNum = []


i = 0
while (i < len(cpfInput)):  #Transfere apenas numeros    ################ ADICIONAR O FILTRO PARA APENAS NUMEROS, PONTO E TRAÇO

    if (cpfInput[i] == '.' or cpfInput[i] == '-'):
        i+=1
    else: 
        cpfNum.append(int(cpfInput[i]))
        i+=1

# print(cpfInput)
# print(cpfNum)

if (len(cpfNum) == 11):
    
    i = 0
    n1 = 10
    valNum1 = 0
    while (i < 9):  # PRIMEIRO DIGITO
        valNum1 = (cpfNum[i] * n1) + valNum1
        i+=1
        n1-=1
    
    i=0
    n2 = 11
    valNum2 = 0
    while (i < 10): # SEGUNDO DIGITO
        valNum2 = (cpfNum[i] * n2) + valNum2
        i+=1
        n2-=1

    valNum1 = 11 - (valNum1 % 11)
    valNum2 = 11 - (valNum2 % 11)

    if (valNum1 > 9): #Primeiro calc igual a 0
        valNum1 = 0

    elif (valNum2 > 9): #Segundo calc igual a 0
        valNum2 = 0

    elif (valNum1 > 9 and valNum2 > 9): #Ambos iguais a zero
        valNum1 = 0
        valNum2 = 0

    print(valNum1, valNum2)

    if (valNum1 == cpfNum[-2] and valNum2 == cpfNum[-1]):
        print("-"*11)
        print("CPF Válido!")
        print("-"*11)


else:
    print("-"*13)
    print("CPF Inválido!")
    print("-"*13)

# print(valfinal)