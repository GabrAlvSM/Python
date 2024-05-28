# Faça um algoritmo que receba o número de avaliações do estudante que será (utilizado como contador), após receba as notas e apresente a média do estudante.

num = int(input("Digite a quantidade de avaliações: "))
notas = []

while len(notas) < num :

    notaAdd = float(input(f"Digite a {len(notas) + 1}ª nota do aluno: "))
    notas.append(notaAdd)
    
    if len(notas) == num:
        
        soma = 0
        for nota in notas:
            soma = soma + nota
            

        media = soma / num
        print(f"A média do aluno foi: {media}")
          