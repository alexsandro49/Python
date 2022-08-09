def resumo(v=0, aum=0, dim=0):
    print('=-='*10)
    print('     RESUMO DO VALOR     ')
    print('=-='*10)
    print(f'Preço analisado: \tR${v:.1f}'.replace('.',','))
    print(f'Dobro do preço: \tR${dobro(v):.1f}'.replace('.',','))
    print(f'Metade do preço: \tR${metade(v):.1f}'.replace('.',','))
    print(f'{aum}% de aumento: \tR${aumento(v, aum):.1f}'.replace('.',','))
    print(f'{dim}% de redução: \tR${reducao(v, dim):.1f}'.replace('.',','))
    print('=-='*10)

def dobro(n):
    n *= 2
    return n

def metade(n):
    n = n / 2
    return n

def aumento(n, aum=0):
    n = n + (n * aum/100)
    return n

def reducao(n, dim=0):
    n = n - (n * dim/100)
    return n
