# Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de 
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente 
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
# como nota de aprovação.

## MELHORADO - Sistema de média funcional com calculo automático de média com o usuário apenas inserindo as notas

notas_lista = []

while (True):
    nota = input("Digite uma nota: ")

    if nota == '':
        print(f"\n{len(notas_lista)} notas adicionadas.\n")
        break

    else:
        nota = int(nota)

        if 0 <= nota <= 10:
            notas_lista.append(nota)
            print(f"Notas já contabilizadas: \n{notas_lista}")
        else:
            print("\n--Notas válidas apenas de 0 a 10!--\n")

# print(notas_lista, "lista de notas adicionadas")

soma = 0
i=0
while (i != len(notas_lista)):
    x = notas_lista[i]
    soma += x
    i+=1

media = soma / len(notas_lista)

print(f"A média do aluno é: {media}")