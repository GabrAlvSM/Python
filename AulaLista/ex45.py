peq = int(input("Digite a quantidade de camisetas pequenas na sacola: "))
med = int(input("Digite a quantidade de camisetas médias na sacola:  "))
grand = int(input("Digite a quantidade de camisetas grandes na sacola:  "))

total = (peq * 35) + (med * 45) + (grand * 55)

print(f"O valor total da sacola é de R${total}, sendo {peq} pequenas, {med} medias, {grand} grandes")
