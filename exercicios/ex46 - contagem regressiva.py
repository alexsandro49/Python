#Uma contagem regressiva de 10 até 0.

from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(0.5)
print('FIM DA CONTAGEM!')
