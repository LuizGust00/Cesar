import streamlit as st
import json
import os
from src.controlers.encriptado import *
from src.models.classes import *
from src.controlers.chat_defs import *

#session_state
if "login" not in st.session_state:
    st.session_state.login = Usuario
if "logado" not in st.session_state:
    st.session_state.logado = False

#Nome de usuário
user_name = st.text_input("Coloque seu nome")
nome_existe = existe_usuario(user_name)
if not (nome_existe) or (user_name == ""):
    st.error("Usuário não existe")
else:
    st.success("Usuário existe")

#A senha do usuário
senha_user = st.text_input("Digite uma senha")
if senha_user == "":
    st.error("Digite uma senha")
else:
    st.success("Senha Válida")

#Botão para fazer login
if st.button("Login"):
    login = fazer_login(user_name, senha_user)
    if isinstance(login, str):
        st.error(login)
    else:
        st.session_state.login = login
        st.session_state.logado = True
        st.switch_page('pages/contatos.py')