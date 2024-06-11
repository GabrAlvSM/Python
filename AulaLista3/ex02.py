# Crie um programa que determine o mostre os 5 primeiros números ímpares, considerando 
# números maiores que 0

num = []
x = 0

while (len(num) != 5):
    x = x + 1
    if x % 2 != 0:
        num.append(x)
        print(x)