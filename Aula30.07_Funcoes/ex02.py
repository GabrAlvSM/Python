# 2 – Crie uma função para calcular a exponenciação, que necessite dois argumentos e apresente como resultado a potência. Sendo base elevado ao expoente.

def potenc(x,y):
    res = x ** y
    return res

val1 = int(input("Digite a base: "))
val2 = int(input("Digite o expoente: "))

x = potenc(val1,val2)

print(f"Resposta: {x}")