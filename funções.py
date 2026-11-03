import sqlite3
from menus import menuGrafico

connect = sqlite3.connect("financeiro.db")
cursor = connect.cursor()
conexao.row_factory = sqlite3.Row
dados = cursor.fetchall()
#======================
#FUNÇÕES MENU PRINCIPAL
#======================

def registroDeEntrada():
    print('='*33)
    print(f'{' Registro de Entrada ':=^33.33}')
    print('='*33)
    entrada = float(input('Digite o valor a ser registrado: '))
    origem = input('Digite a origem do valor [Salario/FreeLancer/Extra/etc...]: ')
    print('='*33)
    print('Digite a data de hoje.')
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))

    if entrada > 0:
        cursor.execute(f"""INSERT INTO registro_entrada (valor , origem, data) VALUES 
                        ({entrada}, "{origem}", "{ano}-{mes}-{dia}")
                        """)

        print('Entrada Registrada.')

    else: 
        print('Não foi possivel realizar o registro')


def registroDeSaida():
    print('='*33)
    print(f'{' Registro de Saida ':=^33.33}')
    print('='*33)
    entrada = float(input('Digite o valor a ser registrado: '))
    origem = input('Digite a origem da saida/gasto: ')
    print('='*33)
    print('Digite a data de hoje.')
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))

    if entrada > 0:
        cursor.execute(f"""INSERT INTO registro_saida (valor , origem, data) VALUES 
                        ({entrada}, "{origem}", "{ano}-{mes}-{dia}")
                        """)

        print('Saida Registrada.')

    else: 
        print('Não foi possivel realizar o registro')


def registros():
    menuGrafico()
    função = int(input('Digite a função que deseja usar: '))

    if função == 1:
        cursor.execute("""SELECT * FROM registro_entrada""")

        print(f'|ID{'':.>5.5}|{'VALOR':.>10.10}|{'ORIGEM':.>15.15}|{'DATA':.>10.10}|')

        for registro in dados:
            print(f'|{registro['id']:.>5.5}|{registro['valor']:.>10.10}|{registro['origem']:.>15.15}|{registro['data']:.>10.10}|')
            
            


    elif função == 2:
        cursor.execute("""SELECT * FROM registro_saida""")