# Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número
# fornecido é primo ou não.


# if (num % 2 != 0 and num % 3 != 0 or num == 2 or num == 3):
#     print("primo!")
# else:
#     print("não primo!")

#####      Divide the given number by all the prime numbers below its square root value

# while (True):

#     if (num == 0):
#         print("Fim!")
#         break


num = float(input("\nDigite um número: "))

raizNum = num**(1/2)


while (num > 0):
            
    if (num % 2 != 0 and num > 3):
        i=3
        while(i < raizNum):
            if (num % i == 0):
                print("não primo!")
                break
            i+=2
        if (i >= raizNum):
            print("primo")
        break
    
    elif (num % 2 == 0 and num != 2):
        print("não primo!")
        break

    else:
        print("primo!")
        break
        
print("Fim!\n")
