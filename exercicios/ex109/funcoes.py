def metade(n, formato=False):
    n = n / 2
    return n if not formato else moeda(n)
def dobro(n, formato=False):
    n *= 2
    return n if not formato else moeda(n)

def aumento(n, formato=False):
    porc10 = n * 0.1
    n = n + porc10
    return n if not formato else moeda(n)

def moeda(valor = 0, cifrao = 'R$'):
    return f'{cifrao}{valor:.1f}'.replace('.',',')
