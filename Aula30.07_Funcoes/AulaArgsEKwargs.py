def calc(**kwargs):
    print(kwargs)
    val = kwargs['valor']
    perc = kwargs['porcentagem']
    res = val * perc / 100
    return res

x = calc(idade=18,cidade="CG", valor=1000,porcentagem=10 )

print(x)