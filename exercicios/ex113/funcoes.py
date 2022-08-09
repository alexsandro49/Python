def ValorInteiro(v):
    while True:
        try:
            valor = int(input(v))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mErro: Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return valor
            
def ValorReal(v):
    while True:
        try:
            valor = float(input(v))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mErro: Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return valor

