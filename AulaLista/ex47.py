valhr = 32.5
valhrex = 44.5

qntHr = int(input("Digite a quantidade de horas normais trabalhadas: "))
qntHrEx = int(input("Digite a quantidade de horas extras trabalhadas: "))

hrtotal = qntHr + qntHrEx

salBrut = (valhr * qntHr) + (valhrex * qntHrEx)
salLiqu = ((valhr * qntHr) + (valhrex * qntHrEx)) * 0.89

print(f"A quantidade dehoras trabalhadas totais é de {hrtotal}, sendo {qntHr} de horas normais e {qntHrEx} de horas extras.")
print(f"O valor do salário bruto é de R${salBrut}, e com descontos é de R${salLiqu}.")