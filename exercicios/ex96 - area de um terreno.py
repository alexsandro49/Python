#Usando funções, monta um programa para medir a área de um terreno.

def linha():
    print('-'*30)
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')


linha()
print(f'{"Controle de terrenos":^30}')
linha()
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
linha()
