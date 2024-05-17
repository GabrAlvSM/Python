from math import sqrt

cordx1 = int(input("Digite a coordenada de x do primeiro ponto: "))
cordy1 = int(input("Digite a coordenada de y do primeiro ponto: "))

cordx2 = int(input("Digite a coordenada de x do segundo ponto: "))
cordy2 = int(input("Digite a coordenada de y do segundo ponto: "))


distan = sqrt(((cordx1 - cordy1)**2) + ((cordx2 - cordy2)**2))

if (distan >= 10) :
    print("Longe!")
else: 
    print("Perto!")