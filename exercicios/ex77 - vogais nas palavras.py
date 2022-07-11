#Mostra quais vogais existem nas palavras definidas.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
print('=-='*12)
print('')
for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c].upper()} temos', end=' ')
    if 'a' in palavras[c]:
        print(f'a', end=' ')
    if 'e' in palavras[c]:
        print(f'e', end=' ')
    if 'i' in palavras[c]:
        print(f'i', end=' ')
    if 'o' in palavras[c]:
        print(f'o',end=' ')
    if 'u' in palavras[c]:
        print(f'u', end=' ')
    print('\n')
print('=-='*12)

