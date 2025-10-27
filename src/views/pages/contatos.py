import streamlit as st
import json
import os
from src.controlers.encriptado import *
from src.models.classes_chat import *

nome_banco_dados = "banco_dados_chat.db"
pasta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
caminho_banco_dados = os.path.join(pasta_raiz, 'src', 'data', nome_banco_dados)

if "meu_usuario" not in st.session_state:
    st.session_state.meu_usuario = Usuario
if "logado" not in st.session_state:
    st.session_state.logado = False

print(st.session_state.meu_usuario.nome)
if st.session_state.logado:
    #Seleciona um dos usuários para conversa
    try:
        with sqlite3.connect(caminho_banco_dados) as conexao:
            cursor = conexao.cursor()
            lista_ids = Usuario.lista_id(cursor, [st.session_state.meu_usuario.id])
            contato_selet = st.selectbox(
                "Com quem vai falar",
                (Usuario.achar_id_nome(cursor, id=id) for id in lista_ids),
                index=None,
                placeholder="Selecione um contato",
            )
    except Exception as e:
        lista_ids = []
        print(f'Ocorreu um erro ou lista os ids para o usuário: <{st.session_state.meu_usuario.nome}> ERRO: <{e}>')
    
    
    # if st.button("Conversa"):
    #     caminho_conversa_pv = caminho_para_chat_pv(st.session_state.login['nome'], contato_selet)
    #     st.session_state.caminho_pv = caminho_conversa_pv
    #     st.session_state.destinatario_pv = contato_selet
    #     st.session_state.conversando_pv = True
    #     st.switch_page('pages/conversa_pv.py')
else:
    st.error("Você não está logado")