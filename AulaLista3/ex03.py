# Crie um programa que determine o mostre os 10 primeiros números pares, considerando 
# números maiores que 0.

num = []
x = 0

while (len(num) != 10):
    x = x + 1
    if x % 2 == 0:
        num.append(x)
        print(x)