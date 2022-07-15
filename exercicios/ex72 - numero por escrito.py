#Lê um número, depois o escreve por escrito.

escrito = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 
           'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {escrito[numero]}.')
        break
