import streamlit as st
import json
import os
from src.controlers.encriptado import *
from src.models.classes import *

pasta_raiz = os.path.dirname(os.path.abspath(__file__))
pasta_chat_data = os.path.join(pasta_raiz, "chat_data")
user_file = os.path.join(pasta_chat_data, "usuarios.json")
chats_pasta = os.path.join(pasta_chat_data, "chats")

st.switch_page("pages/criar_usuario.py")


