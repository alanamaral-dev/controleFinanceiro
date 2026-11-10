from dados import saldo, carregar_saldo

def menuPrincipal():
    global saldo
    saldo = carregar_saldo()
    print(f'{'='*60}')
    print(f'={'Controle Financeiro':=^33.33}{' Saldo ':=^9.9} -----> \033[32m{saldo:^7}\033[0m =')
    print(f'{'='*60}')
    print(f'[1]{'Registrar Entrada':.>57.57}')
    print(f'[2]{'Registrar Saida':.>57.57}')
    print(f'[3]{'Gráfico de Registros':.>57.57}')
    print(f'[0]{'Sair':.>57.57}')
    print(f'{'='*60}')


def menuGrafico():
    print("="*33)
    print(f'{'Gráfico de Registros':=^33.33}')
    print("="*33)
    print(f'[1]{'Registros de Entrada':.>30.30}')
    print(f'[2]{'Registros de Saida':.>30.30}')
    print(f'[0]{'Voltar':.>30.30}')
    print("="*33)