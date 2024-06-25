# Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020
# recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do 
# ano anterior. Faça um programa que determine o salário atual do funcionário.

from datetime import date

sal = 4000  #2019
aumen = 0.015

# sal2020 = sal * aumen
ano_inicial = 2019

ano_atual = date.today().year

sal_atual = sal
i=ano_inicial
while (i!=ano_atual):
    sal_atual += sal_atual * aumen
    aumen *= 2
    i+=1
    print(sal_atual)

print(sal_atual)