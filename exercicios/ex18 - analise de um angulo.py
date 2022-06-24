#Mostra o seno, cosseno e a tangente de um ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tang:.2f}')
