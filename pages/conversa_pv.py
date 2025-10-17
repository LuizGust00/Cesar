import streamlit as st
import json
import os
from datetime import datetime
from src.controlers.encriptado import *
from src.models.classes import *
from src.controlers.chat_defs import *

pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_chat_data = os.path.join(pasta_raiz, "chat_data")
user_file = os.path.join(pasta_chat_data, "usuarios.json")
chats_pasta = os.path.join(pasta_chat_data, "chats")

if "logado" not in st.session_state:
    st.session_state.conversando_pv = False
if "caminho_pv" not in st.session_state:
    st.session_state.caminho_pv = None
if "conversando_pv" not in st.session_state:
    st.session_state.conversando_pv = False
if "destinatario_pv" not in st.session_state:
    st.session_state.destinatario_pv = ""

if st.session_state.conversando_pv:
    user_nome = st.session_state.login['nome']
    caminho = st.session_state.caminho_pv
    destinatario = st.session_state.destinatario_pv
    chave_privada = st.session_state.login['chaves'][0]

    st.title(destinatario)

    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for item in json.load(f):
                if user_nome == item['nome']:
                    codigo = item['mensagem_eu']
                    mensagem = descriptografar(codigo, chave_privada)
                    texto_alinhado(mensagem, 'right')
                else:
                    codigo = item['mensagem_destinatario']
                    mensagem = descriptografar(codigo, chave_privada)
                    texto_alinhado(mensagem, 'left')
    except Exception as e:
        st.error(f"Conversa não encotrada {e}")

    texto = st.text_input("Mensagem para enviar")
    if st.button("Enviar"):
        enviar_mensagem_pv(caminho, user_nome, destinatario, texto)
        st.rerun()
    
else:
    st.error("Você não está logado")