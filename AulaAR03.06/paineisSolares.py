# Calcular quantidade de painéis solares para uma residência. 

# Fórmula — [Potência do painel X Irradiação (1 – Percentual de perda)];

# 550Wp (Watts pico) - até 2.200Wh/dia (máximo em condições ideais)
# 20% de perda
# irradição 5kWh/m²


### Energia = potência do módulo solar x tempo x (rendimento)

placa = 265
perda = 0.2
irradiac = 5

placagera = ((placa * irradiac * (1 - perda))/1000) * 30

consumo = float(input("Informe quantos kWh são gastos por mês na casa: "))

qntPlacas = consumo / placagera

print(f"O consumo da casa equivale a aproximadamente {round(qntPlacas)} placas de {placa}Wp que geram individualmente {placagera}kWh de energia mensal.")