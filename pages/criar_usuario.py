import streamlit as st
import json
import os
from src.controlers.encriptado import *
from src.models.classes import *
from src.controlers.chat_defs import *

pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_chat_data = os.path.join(pasta_raiz, "chat_data")
user_file = os.path.join(pasta_chat_data, "usuarios.json")
chats_pasta = os.path.join(pasta_chat_data, "chats")

#session_state
if "login" not in st.session_state:
    st.session_state.login = []
if "logado" not in st.session_state:
    st.session_state.logado = False

login_valido = True

#Nome de usuário
user_name = st.text_input("Coloque seu nome")
nome_existe = existe_usuario(user_name)
if isinstance(nome_existe, str):
    st.error(nome_existe)
    login_valido = False
elif nome_existe:
    st.error("Nome já existente")
    login_valido = False
else:
    st.success("Nome disponível")

#A senha do usuário
senha_user = st.text_input("Digite uma senha")
if senha_user == "":
    login_valido = False
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
    login_valido = False
else:
    st.success(f"Chaves privadas: {chaves[0]} e públicas: {chaves[1]}")

#Botão para criar
if st.button("Criar") and login_valido:
    login = adicionar_usuario(user_name, senha_user, chaves)
    if isinstance(login, str):
        st.error(login)
    else:
        st.session_state.login = login
    st.session_state.logado = True
    st.switch_page('pages/contatos.py')
    st.rerun()