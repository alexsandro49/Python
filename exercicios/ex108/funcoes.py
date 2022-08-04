def metade(n):
    n = n / 2
    return n
def dobro(n):
    n *= 2
    return n

def aumento(n):
    porc10 = n * 0.1
    n = n + porc10
    return n

def moeda(valor = 0, cifrao = 'R$'):
    return f'{cifrao}{valor:.1f}'.replace('.',',')
