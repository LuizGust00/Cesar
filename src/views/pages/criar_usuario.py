import streamlit as st
import json
import os
from src.controlers.encriptado import *
from src.models.classes import *
from src.models.classes_chat import *
from src.controlers.chat_defs import *

nome_banco_dados = "banco_dados_chat.db"
pasta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
caminho_banco_dados = os.path.join(pasta_raiz, 'src', 'data', nome_banco_dados)

#session_state
if "meu_usuario" not in st.session_state:
    st.session_state.meu_usuario = Usuario
if "logado" not in st.session_state:
    st.session_state.logado = False

criar_bool = True

#Nome de usuário
nome_digitado = st.text_input("Coloque seu nome")
try:
    with sqlite3.connect(caminho_banco_dados) as conexao:
        cursor = conexao.cursor()
        nome_existe = Usuario.usuario_existe(cursor, nome_digitado)
except Exception as e:
    nome_existe = True
    print(f'Ocorreu um erro ou verificar se existia o usuário: <{nome_digitado}> para criação de usuário: <{e}>')

if nome_existe:
    st.error("Nome já existente")
    criar_bool = False
else:
    st.success("Nome disponível")

#A senha do usuário
senha_digitada = st.text_input("Digite uma senha")
if senha_digitada == "":
    criar_bool = False
    st.error("Digite uma senha")
else:
    st.success("Senha Válida")

#Os parâmetros do usuário
p = st.number_input("Digite um primo para p", step=1, value=11)
q = st.number_input("Digite um primo para q", step=1, value=13)
e = st.number_input("Digite o expoente e (coprimo de φ(n))", step=1, value=73)

chaves = validar_numeros(p, q, e)
if isinstance(chaves, str):
    st.error(chaves)
    criar_bool = False
else:
    st.success(f"Chaves privadas: {chaves[0]} e públicas: {chaves[1]}")

#Botão para criar
if st.button("Criar Usuário") and criar_bool:
    try:
        with sqlite3.connect(caminho_banco_dados) as conexao:
            usuario = Usuario(nome=nome_digitado, senha=senha_digitada, chave_n=chaves[1][0], chave_e=chaves[1][1], chave_d=chaves[0][1],
                              usuario_teste=True)
            cursor = conexao.cursor()
            usuario.adicionar(cursor)
            conexao.commit()
            st.session_state.meu_usuario = usuario
    except Exception as e:
        print(f'Ocorreu um erro ou tentar adicionar o usuário: <{nome_digitado}>; ERRO: <{e}>')
    st.session_state.logado = True
    #st.switch_page('pages/contatos.py')
    st.rerun()