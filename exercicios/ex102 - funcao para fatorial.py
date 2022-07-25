#Cálculo de fatorial, tendo o parâmetro show como opcional da escrita do cálculo.
#Docstring adicionada a função "fatorial()".

def fatorial(n, show = False):
    '''
    -> Calcula o fatorial de um número.
    :param n: número  para o cálculo.
    :param show: mostra o cálculo (opcional).
    :return:
    '''
    c = n - 1
    res = n
    while c > 0:
        res *= c
        if show:
            if c == n - 1:
                print(f'{n} x' , end=' ')
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        c -= 1
    return res

print(fatorial(5, show=True))
