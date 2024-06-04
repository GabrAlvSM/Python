cidades = ["Fortaleza", "Bonito", "Rolândia", "Entrepelado", "Sombrio", "Pintópolis", "Anta Gorda", "Jijoca de Jericoacoara", "Paudalho", "Curralinhos", "Ponta Grossa"]
num_letras_por_cidade = {}

for cidade in cidades:
    num_letras = 0

    for letra in cidade:
        num_letras += 1

    num_letras_por_cidade[cidade] = num_letras


cidades_ordem_decrescente = []

while num_letras_por_cidade:
    maior_num_letras = -1
    cidade_maior_num_letras = None

    for cidade, num_letras in num_letras_por_cidade.items():

        if num_letras > maior_num_letras:
            maior_num_letras = num_letras
            cidade_maior_num_letras = cidade

    cidades_ordem_decrescente.append(cidade_maior_num_letras)
    del num_letras_por_cidade[cidade_maior_num_letras]



for cidade in cidades_ordem_decrescente:
    print(cidade)
