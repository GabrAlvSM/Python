valor = float(input("Digite o valor do produto: "))

desc10 = valor * 0.9
parc3 = valor * 0.33
comissvist = desc10 * 0.05
comissparc = valor * 0.05

print(f"O valor com desconto de 10% é de R${desc10}\nCaso deseje parcelar, cada parcela terá o valor de R${parc3}\nA comissão do vendedor para o caso de uma venda a vista é de R${comissvist}\nA comissão do vendedor para o case de uma venda parcelada é de R${comissparc}")
