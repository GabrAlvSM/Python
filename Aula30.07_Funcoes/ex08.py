# 8 – Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do MS (50 Kg) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# O pescador precisa que você crie uma função para ler a quantidade de peixes e calcular o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que o pescador deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

pesoT,valorT = 0.0

def calcExt(pesoTotal, valorT):
    if (pesoTotal > 50):
        pesoExtra = pesoTotal - 50
        multa = pesoExtra * 4

        valorT+=multa

        return (f"Extra pescado: {pesoExtra}Kg \nValor extra a ser pago: {multa}")
    else:
        return (f"Tudo nos conformes!\n Valor total do pescado: {valorT}")


print("\n--Fish-o-matic-3000--\n")

peixes = int(input("Informe a quantidade de pescados: "))

i=0
while peixes > i:
    pesoUni = input(f"{i+1}- Informe o peso do pescado: ")
    valorUni = input(f"{i+1}- Informe o valor por kilo do pescado: ")
    
    valorT += pesoUni * valorUni

    i+=1