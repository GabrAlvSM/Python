paoz = int(input("Digite a quantidade de pãezinhos vendidos: "))
broa = int(input("Digite a quantidade de broas vendidadas: "))

paoztot = paoz * 0.12
broatot = broa * 1.5

total = (paoztot + broatot)
guadar = total * 0.1

print(f"A quantidade de produtos vendidos é de: {paoz} pãezinhos e {broa} broas")

print(f"O valor total de produtos vendidos é de R${total}")
print(f"O valor que deve ser colocado na poupança é de R${guadar}")