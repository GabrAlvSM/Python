qntvend = int(input("Digite a quantidade sanduíches que serão feitos: "))

hamb = 100
pres = 50
queij = 50

qntHamb = (hamb * qntvend) /1000
qntPres = (pres * qntvend) /1000
qntQueij = (queij * qntvend) /1000

print(f"A quantide de produpos para a compra é de: \n{qntHamb}Kg de Carne;\n{qntPres}Kg de presunto;\n{qntQueij}Kg de queijo")
