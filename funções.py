import sqlite3
import os
from menus import menuGrafico
from dados import saldo, salvar_saldo

connect = sqlite3.connect("financeiro.db")
cursor = connect.cursor()
connect.row_factory = sqlite3.Row
dados = cursor.fetchall()

#===================
#FUNÇÕES DO TERMINAL
#===================

def limpar_tela():
    # os.name vale 'nt' no Windows. Em Linux/Mac vale 'posix'.
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione Enter para continuar...")


#======================
#FUNÇÕES MENU PRINCIPAL
#======================

def registroDeEntrada():

    global saldo

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

        print('\033[32m[Entrada Registrada.]\033[0m')
        connect.commit()
        saldo += entrada

        salvar_saldo(saldo)

    else: 
        print('\033[31mNão foi possivel realizar o registro\033[0m')


def registroDeSaida():

    global saldo

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

        print('\033[32m[Saida Registrada.]\033[0m')
        connect.commit()
        saldo -= entrada

        salvar_saldo(saldo)

    else: 
        print('\033[31mNão foi possivel realizar o registro\033[0m')


def registros():
    menuGrafico()
    função = int(input('Digite a função que deseja usar: '))

    if função == 1:
        limpar_tela()
        cursor.execute("""SELECT * FROM registro_entrada""")
        dados = cursor.fetchall()

        print('='*47)
        print(f'{' Registros De Entrada ':-^47}')
        print('='*47)
        print(f'+-------+----------+---------------+----------+')
        print(f'|{'ID':.>7.7}|{'VALOR':.>10.10}|{'ORIGEM':.>15.15}|{'DATA':.>10.10}|')
        print(f'+-------+----------+---------------+----------+')

        for i in range(len(dados)):
            j = 0
            print(f'|{dados[i][j]:.>7}|{dados[i][j+1]:.>10}|{dados[i][j+2]:.>15}|{dados[i][j+3]:.>10}|')
            print(f'+-------+----------+---------------+----------+')


    elif função == 2:
        limpar_tela()
        cursor.execute("""SELECT * FROM registro_saida""")
        dados = cursor.fetchall()

        print('='*47)
        print(f'{' Registros De Saída ':-^47}')
        print('='*47)
        print(f'+-------+----------+---------------+----------+')
        print(f'|{'ID':.>7.7}|{'VALOR':.>10.10}|{'ORIGEM':.>15.15}|{'DATA':.>10.10}|')
        print(f'+-------+----------+---------------+----------+')

        for i in range(len(dados)):
            j = 0
            print(f'|{dados[i][j]:.>7}|{dados[i][j+1]:.>10}|{dados[i][j+2]:.>15}|{dados[i][j+3]:.>10}|')
            print(f'+-------+----------+---------------+----------+')