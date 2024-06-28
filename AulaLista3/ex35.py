# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

consoantes = ['a','e','i''o','u']

palavra = str(input("Digite 10 caracteres alatórios: "))

if (len(palavra) == 10):

    palavra = str(palavra.lower)
    
    i=0
    contador = 0
    while i < len(palavra):

        if palavra[i] == 'a' or palavra[i] == 'e' or palavra[i] == 'i' or palavra[i] == 'u':
            contador+=1
            # print(f"Posição {i+1} da lista: {palavra[i]}")
        elif palavra[i] == '':
            break
        i+=1
        print(contador)
    
    print(contador)
else:
    print("O vetor deve possuir 10 caracteres!")