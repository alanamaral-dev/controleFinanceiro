from funções import registroDeEntrada
from funções import sqlite3, cursor, connect

cursor.execute("""CREATE TABLE IF NOT EXISTS registro_entrada (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                valor FLOAT NOT NULL, 
                origem VARCHAR(100) NOT NULL, 
                data DATE NOT NULL,
                id_saida INTEGER NOT NULL,  
                FOREIGN KEY (id_saida) REFERENCES registro_saida(id))
                """)

cursor.execute("""CREATE TABLE IF NOT EXISTS registro_saida (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                valor FLOAT NOT NULL, 
                origem VARCHAR(100) NOT NULL, 
                data DATE NOT NULL)
                """)