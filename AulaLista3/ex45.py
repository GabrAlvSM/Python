# O funcionário chamado Carlos tem um colega chamado João que recebe um salário que é 
# equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança
# e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João irá aplicar seu 
# salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um 
# programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor 
# pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores 
# para as taxas.

salCarlos = 6000
salJoao = 2000

meses = 1 

while salJoao < salCarlos:
    salCarlos += salCarlos * 0.02
    salJoao += salJoao * 0.05

    print(f"{meses} Carlos: {salCarlos:.2f}")
    print(f"{meses} Joao{salJoao:.2f}\n")
    meses+=1

print(meses)