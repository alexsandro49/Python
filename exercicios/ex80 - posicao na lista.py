#Ler 5 valores, organizando sua posição por ordem crescente na lista.

lista = []

for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao fim da fila.')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adicionado na posição {posicao}.')
                break
            posicao += 1
print(lista)
