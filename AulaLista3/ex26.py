# Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3 
# x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente 
# (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para 
# resolver o problema utilize estrutura de repetição.

base = int(input("base: "))
expoente = int(input("exp: "))

x = base
i=1
while expoente > i:
    x = x * base
    
    i+=1

print(f"\n{base}^{expoente} = {x}\n")