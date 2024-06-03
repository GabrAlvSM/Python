# Um algoritmo em que usuário escolha uma opção de acordo com o último número da placa do carro e mostre uma mensagem dizendo em que dia da semana não poderá circular. 
# 1 - 2 “Não Circular 2ª Feira” 
# 3 - 4 “Não Circular 3ª Feira” 
# 5 - 6 “Não Circular 4ª Feira” 
# 7 - 8 “Não Circular 5ª Feira” 
# 9 - 0 “Não Circular 6ª Feira” 

placa = int(input("Digite o último número da sua placa: "))

if (0 <= placa <= 9):
    if (1 <= placa <= 2):
        print("O carro não poderá circular na 2ª Feira")
    if (3 <= placa <= 4):
        print("O carro não poderá circular na 3ª Feira")
    if (5 <= placa <= 6):
        print("O carro não poderá circular na 4ª Feira")
    if (7 <= placa <= 8):
        print("O carro não poderá circular na 5ª Feira")
    if (placa == 9 or placa == 0):
        print("O carro não poderá circular na 6ª Feira")

else:
    print("Apenas o dígito final da placa!")