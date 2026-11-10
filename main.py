from funções import registroDeEntrada, registroDeSaida, registros, limpar_tela, pausar
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
        limpar_tela()
        menuPrincipal()
        funcao = int(input("Digite a função que deseja utilizar: "))

        if funcao == 1:
            limpar_tela()
            registroDeEntrada()
            pausar()

        elif funcao == 2:
            limpar_tela()
            registroDeSaida()
            pausar()

        elif funcao == 3:
            limpar_tela()
            registros()
            pausar()


        elif funcao == 0:
            limpar_tela()
            print("[Programa Finalizado!]")
            break

    except:
        print("\033[31m[Valor digitado invalido]\033[0m")
        pausar()

