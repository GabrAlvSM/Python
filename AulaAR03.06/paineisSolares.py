# Calcular quantidade de painéis solares para uma residência. Para implementar as quatro demandas acima, 
# você deverá listar os requisitos necessários para o desenvolvimento, elaborar o diagrama de caso de uso e por fim o algoritmo utilizando o Python.

# Fórmula — [Potência do painel X Irradiação (1 – Percentual de perda)];

# 550Wp (Watts pico) - até 2.200Wh/dia (máximo em condições ideais)
# 20% de perda
# irradição 5kWh/m²


### Energia = potência do módulo solar x tempo x (rendimento)

placa = 550
perda = 0.2
irradiac = 5

placagera = placa * irradiac * (1-perda)

consumo = float(input("Informe quantos kWh são gastos por mês na casa: "))

print(placagera)