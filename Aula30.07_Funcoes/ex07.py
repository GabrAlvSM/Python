# 7 – Crie uma função que efetue o cálculo do salário e como retorno teremos o valor a ser pago conforme o número de horas trabalhadas. 
# Considere a carga horária de 40h por semana como salário base, caso ultrapasse o limite de 40h, o funcionário deve receber 50% a mais por hora excedente.


def calcSalario(salarioHora, horasTrab):

    if horasTrab > 40:
        salario = salarioHora * 40
        
        hExtra = ((horasTrab - 40) * salarioHora) * 1.5

        salario += hExtra

    else:
        salario = salarioHora * horasTrab


    return salario


salH = float(input("Informe o valor do salario/hora: "))
horaT= int(input("Informe a quantidade de horas trabalhadas pelo funcionário: "))

print(calcSalario(salH,horaT))