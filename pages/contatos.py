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

if "login" not in st.session_state:
    st.session_state.login = Usuario
if "logado" not in st.session_state:
    st.session_state.logado = False
if "caminho_pv" not in st.session_state:
    st.session_state.caminho_pv = None
if "conversando_pv" not in st.session_state:
    st.session_state.conversando_pv = False
if "destinatario" not in st.session_state:
    st.session_state.destinatario_pv = ""

if st.session_state.logado:
    #Seleciona um dos usuários para conversa
    contato_selet = st.selectbox(
    "Com quem vai falar",
    (nome for nome in lista_usuarios(st.session_state.login['nome'])),
    index=None,
    placeholder="Selecione um contato",
    )

    if st.button("Conversa"):
        caminho_conversa_pv = caminho_para_chat_pv(st.session_state.login['nome'], contato_selet)
        st.session_state.caminho_pv = caminho_conversa_pv
        st.session_state.destinatario_pv = contato_selet
        st.session_state.conversando_pv = True
        st.switch_page('pages/conversa_pv.py')
else:
    st.error("Você não está logado")