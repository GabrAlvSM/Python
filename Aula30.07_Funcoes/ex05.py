# 5 – Escreva um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. Por fim deve retornar o novo valor para o usuário considerando o percentual do imposto.

def somaImposto(taxaImposto, custo):
    if taxaImposto != 0:
        taxaImposto = taxaImposto/100
    
        valorImposto = taxaImposto * custo

        total = valorImposto + custo
        return f"\nValor total: {total} \nValor do imposto: {valorImposto}"
    
    else:
        return f"\nNão possui imposto! \nValor total: {custo}"


custo = float(input("Digite o valor do custo: "))
imposto = int(input("Digite a porcentagem do imposto(0 a 100): "))

print(somaImposto(imposto,custo))