#Usando funções cria duas contagens,
#pedindo para o usuário montar as condições da última contagem.

from time import sleep

def linha():
    print('-=-'*15)
def contagem(i, f, p):
    for c in range(i, f+1, p):
        print(c, end=' ', flush=True)
        sleep(0.2)
    print('FIM!')
sleep(0.5)
linha()
sleep(0.2)
print(f'{"Contagem de 1 até 10 de 1 em 1":^40}')
contagem(1, 10, 1)
sleep(0.5)
linha()
sleep(0.2)
print(f'{"Contagem de 10 até 11 de 2 em 2":^40}')
contagem(10, -2, -2)
sleep(0.5)
linha()
sleep(0.2)
print(f'{"Denfina as condições da contagem: ":^40}')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
linha()
sleep(0.2)
print(f'   Contagem de {i} até {f} de {p} em {p}')
if i > f:
    f -= 2
    contagem(i, f, -p)
else:
    contagem(i, f, p)
linha()
