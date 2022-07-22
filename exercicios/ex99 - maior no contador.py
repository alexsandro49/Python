#Um contador que indica o maior valor entre os apresentados.

def linha():
    print('=-='*15)
def analise(* num):
    contador = maior = 0
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end=' ')
        if contador == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


linha()
analise(2, 9, 4, 5, 7, 1)
linha()
analise(4, 7, 0)
linha()
analise(1, 2)
linha()
analise(6)
linha()
analise()
linha()
