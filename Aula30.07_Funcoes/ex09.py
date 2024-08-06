# 9 – O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, a principal função do sistema é calcularTempo(). 
# Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. 
# Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​

valHora:float = 9
valHExtra:float = 1.5

def calcTempo(entrada,saida):
    horaEntrada = entrada[0] + entrada[1]
    horaEntrada = int(horaEntrada)
    minEntrada = entrada[2] + entrada[3]

    
    return 

entrada = input("Informe a hora de entrada do veículo (HH:mm): ")
saida = input("Informe a hora de saída do veículo (HH:mm): ")