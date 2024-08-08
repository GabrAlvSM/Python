# 9 – O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, a principal função do sistema é calcularTempo(). 
# Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. 
# Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​

# Adicione na função calcularTempo() do sistema para estacionamento o valor dos impostos pago pelo cliente. 
# Considere o PIS: 0,33% , COFINS: 0,20% e ICMS: 17% no valor e imprima o recibo do cliente.

def calcTempo(entrada,saida):

    # Lê a hora de entrada
    horaEntrada = entrada[0] + entrada[1]
    horaEntrada = int(horaEntrada)
    minTransfEnt = entrada[3] + entrada[4]
    minTransfEnt = int(minTransfEnt)

    tempoInic = minTransfEnt + horaEntrada * 60
    if (tempoInic > 1439):
        return "Tempo excedido!"

    # Lê a hora de saída
    horaSaida = saida[0] + saida[1]
    horaSaida = int(horaSaida)
    minTransfSai = saida[3] + saida[4]
    minTransfSai = int(minTransfSai)

    tempoSaid = minTransfSai + horaSaida * 60
    if (tempoSaid > 1439):
        return "Tempo excedido!"
    
    tempoTotal = tempoSaid - tempoInic

    return tempoTotal

def pagamento(tempo):
    tempo = tempo

    minutos = tempo%60 
    horas = (tempo / 60)-(minutos/60) # Retirada de minutos
    
    if tempo > 60:
        # valorTotal = (((tempo - 60) / 60) * 1.5) + 9
        if (minutos == 0):
            valorTotal = (horas * 1.5) + 9
        else:
            valorTotal = (horas * 1.5) + 9 + 1.5
    else:
        valorTotal = 9

    if horas > 1 or horas == 0:
        textoTransfH = 'horas'
    else:
        textoTransfH = 'hora'

    if minutos > 1 or minutos == 0:
        textoTransfM = 'minutos'
    else:
        textoTransfM = 'minuto'

    # PIS: 0,33% , COFINS: 0,20% e ICMS: 17%
    piss = 0.0033 * valorTotal
    cofins = 0.0020 * valorTotal
    icms = 0.17 * valorTotal
    impostos = piss + cofins + icms    

    recibo = "Recibo"
    recibo = recibo.center(35, '-')
    endLine = "-"*35


    return f"\n{recibo}\nTempo: {horas:.0f} {textoTransfH} e {minutos} {textoTransfM} \nPIS = R${piss:.2f} \nCOFINS = R${cofins:.2f} \nICMS = R${icms:.2f} \nImpostos = R${impostos:.2f} \nTotal= R${valorTotal}\n{endLine}\n"
    # return f"O valor do estacionamento por {horas:.0f} {textoTransfH} e {minutos} {textoTransfM} é de: R${valorTotal:.2f}"


while True:
    entrada = input("Informe a hora de entrada do veículo (HH:mm): ")
    saida = input("Informe a hora de saída do veículo (HH:mm): ")

    if len(entrada and saida) != 5:
        print("Não! Faz denovo!")
    else:
        break
        
temp = calcTempo(entrada,saida)
print(pagamento(temp))