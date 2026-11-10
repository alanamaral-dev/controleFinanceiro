from funções import registroDeEntrada, registroDeSaida, registros
from funções import sqlite3, cursor, connect
from menus import menuPrincipal

cursor.execute("""CREATE TABLE IF NOT EXISTS registro_entrada (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                valor FLOAT NOT NULL, 
                origem VARCHAR(100) NOT NULL, 
                data DATE NOT NULL)
                """)

cursor.execute("""CREATE TABLE IF NOT EXISTS registro_saida (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                valor FLOAT NOT NULL, 
                origem VARCHAR(100) NOT NULL, 
                data DATE NOT NULL)
                """)

funcao = -1

while funcao != 0:
    try:
        menuPrincipal()
        funcao = int(input("Digite a função que deseja utilizar: "))

        if funcao == 1:
            registroDeEntrada()

        elif funcao == 2:
            registroDeSaida()

        elif funcao == 3:
            registros()


        elif funcao == 0:
            print("[Programa Finalizado!]")
            break

    except:
        print("\033[31m[Valor digitado invalido]\033[0m")

