# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

import os

os.system('cls||clear') #clear terminal


#contadores --
alunos = 10

#contadores ++
i=0
aprovados = 0
soma=0

while (alunos != 0):
    
    nota = (input(f"Digite a {i+1}ª nota: "))
    if nota == '':
        print("A nota não pode estar vazia!")

    else:
        nota = float(nota)

        if (0 <= nota <= 10):
            soma+=nota
            i+=1
        else:
            print("As notas devem estar no intervalo de 0 a 10!")
            
        if (i == 4):
            soma/=4
            if soma >= 7:
                aprovados+=1
                print("Aluno aprovado!\n")
            else:
                print("Aluno reprovado!\n")
            soma = 0
            i=0
            alunos-=1
                
        # print(aluno, aprovados)


if (aprovados>1):
    print(f"{aprovados} alunos aprovados.")
else:
    print(f"{aprovados} aluno aprovado.")