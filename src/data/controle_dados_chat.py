import sqlite3
import os
import json
from src.models.classes_chat import *

nome_banco_dados = "banco_dados_chat.db"
pasta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pasta_data = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_data, nome_banco_dados)

if __name__ == "__main__":
    try:
        with sqlite3.connect(caminho_arquivo) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    chave_n INTEDER NOT NULL,
                    chave_e INTEDER NOT NULL,
                    chave_d INTEDER NOT NULL,
                    logado BOOL DEFAULT TRUE,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    usuario_teste BOOL DEFAULT FALSE,
                    conversas TEXT DEFAULT '[]'
                ) ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS chats(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    integrantes TEXT DEFAULT '[]',
                    ultima_modificacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    chat_teste BOOL DEFAULT FALSE
                ) ''')   
            #cursor.execute('ALTER TABLE usuarios ADD COLUMN conversas TEXT')     
    except Exception as e:
        print(f"Durante a inicialização do banco de dados ocorreu um erro: {e}")

conversa = [14, 17, 19, 7, 6, 4, 1]

try:
    with sqlite3.connect(caminho_arquivo) as conexao:
        user = Usuario(nome='Rodrigo', senha='123664', chave_n=17, chave_e=13, chave_d=27)
        cursor = conexao.cursor()
        #Usuario.modificar(Usuario.achar_id_nome(cursor, nome='Joao'), cursor, conversas=json.dumps(conversa))
        #Usuario.adicionar_conversa(2, cursor, 243)
        #print(Usuario.lista_id(cursor, [1, 2]))
        conexao.commit()
        #print(Usuario.pegar_dado(2, cursor, conversas=True))
except Exception as e:
        print(f"Durante o teste do banco de dados ocorreu um erro: {e}")
