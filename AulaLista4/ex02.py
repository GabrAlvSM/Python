# Faça uma função que receba a data atual (dia, mês e ano) e exiba-a na tela no formato textual 
# por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000.

def formatacao(entrada):
    meses = {
        '01':"janeiro",
        '02':"fevereiro",
        '03':"março",
        '04':"abril",
        '05':"maio",
        '06':"junho",
        '07':"julho",
        '08':"agosto",
        '09':"setembro",
        '10':"outubro",
        '11':"novembro",
        '12':"dezembro"
    }

    i=0
    while (i<len(entrada)):
        if (entrada[i] == '/'):
            pass
        else:
            numeros.append(entrada[i])
        i+=1

    dia:str =''
    mes:str =''
    ano:str =''
    
    if len(numeros) == 8:
        dia = numeros[0] + numeros[1]
        mes = numeros[2] + numeros[3]
        ano = numeros[4] + numeros[5] + numeros[6] + numeros[7]        

        mes:str = meses[dia]
        
    print(f"{dia} de {mes} de {ano}")


data = input("Informe a data atual por extenso(ex: 01/01/2000): ")
numeros = []

formatacao(data)