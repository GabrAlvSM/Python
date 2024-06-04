# Crie um algoritmo que apresente o seguinte resultado:
# *
# **
# ***
# ****

quantid = int(input("Digite a quantide de spam: "))

i=1
while i < quantid:

    print("*" * i)
    i+=1