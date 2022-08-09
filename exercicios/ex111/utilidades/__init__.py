def metade(n, formato=False):
    n = n / 2
    return n if not formato else moeda(n)
def dobro(n, formato=False):
    n *= 2
    return n if not formato else moeda(n)

def aumento(n, aum=0, formato=False):
    porc = n * (aum/100)
    n = n + porc
    return n if not formato else moeda(n)

def reducao(n, dim=0, formato=False):
    n = n - (n * dim/100)
    return n if not formato else moeda(n)

def moeda(valor = 0, cifrao = 'R$'):
    return f'{cifrao}{valor:.1f}'.replace('.',',')

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
    
