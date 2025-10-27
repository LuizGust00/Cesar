import streamlit as st
import json
import os
from datetime import datetime
from src.controlers.encriptado import *
from src.models.classes import *

pasta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pasta_chat_data = os.path.join(pasta_raiz, "chat_data")
user_file = os.path.join(pasta_chat_data, "usuarios.json")
chats_pasta = os.path.join(pasta_chat_data, "chats")

#Adiciona um usuário no arquivo json e retorna o usuário
def adicionar_usuario(nome, senha, chaves):
    novo = Usuario(nome, senha, chaves)
    try:
        with open(user_file, "r", encoding="utf-8") as f:
            arquivo = json.load(f)
    except FileNotFoundError:
        return "Não foi possível achar a lista de usuários"
    except:
        arquivo = []
    
    arquivo.append(vars(novo))
    try:   
        with open(user_file, "w", encoding="utf-8") as f:
            json.dump(arquivo, f, indent=4)
    except:
        return "Não foi possivel salvar o usuario"
    
    return vars(novo)

#Retorna a lista de usuários sem o usuário que foi passado no parametro.
def lista_usuarios(excluir):
    try:
        with open(user_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            lista_user = [item['nome'] for item in data]
    except:
        lista_user = []

    if excluir in lista_user: lista_user.remove(excluir)

    return lista_user

#Retorna o caminho para o arquivo .json de um chat privado
def caminho_para_chat_pv(user1, user2):
    lista_chats = [item.removesuffix(".json") for item in os.listdir(chats_pasta)]
    existe = False
    if user2 == None: return

    for arquivo_nome in lista_chats:
        nomes_user = [n for n in arquivo_nome.split("_")]
        print(nomes_user)
        if user1 in nomes_user and user2 in nomes_user:
            caminho = os.path.join(chats_pasta, arquivo_nome + ".json")
            existe = True
    
    if not existe:
        arquivo_nome = user1 + "_" + user2 + ".json"
        caminho = os.path.join(chats_pasta, arquivo_nome)
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump([], f)
    
    return caminho

#Verifica se o usuário existe
def existe_usuario(user_nome):
    if user_nome == "": return True
    try: 
        with open(user_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            lista_user = [item['nome'] for item in data]
    except:
        return False
    return user_nome in lista_user

#Retorna o usuário com nome passado
def ler_usuario(user_nome):
    try:
        with open(user_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                if item['nome'] == user_nome:
                    return item
        print("Usuário não encontrado")
        return None
    except:
        print("Arquivo não abrio")
        return None

#Verifica as informações para login e retorna o usuário
def fazer_login(user_nome, senha):
    try:
        with open(user_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                if item['nome'] == user_nome and item['senha'] == senha:
                    return item
        return "Nome ou senha inválida"
    except:
        return "Arquivo não encontrado"
    
def enviar_mensagem_pv(caminho, nome_eu, destinatario, texto):
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")

    user_destinatario = ler_usuario(destinatario)
    chave_eu = st.session_state.login['chaves'][1]
    chave_destinatario = user_destinatario['chaves'][1]

    codigo_eu = criptografar(texto, chave_eu)
    codigo_destinatario = criptografar(texto, chave_destinatario)

    mesagem = Mensagem_PV(nome_eu, data, hora, codigo_eu, codigo_destinatario)

    try:
        with open(caminho, "r", encoding="utf-8") as f:
            arquivo = json.load(f)
    except FileNotFoundError:
        return "Não foi possível ler o arquivo da conversa"
    except:
        arquivo = []
    
    #print(vars(mesagem))
    arquivo.append(vars(mesagem))
    #print(arquivo)

    try:   
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(arquivo, f, indent=4)
    except:
        return "Não foi possivel salvar o usuario"

def texto_alinhado(texto: str, alinhamento: str):
    """
    Função para gerar HTML com texto alinhado.
    
    Args:
        texto (str): O texto a ser exibido.
        alinhamento (str): 'left', 'center', ou 'right'.
    """
    st.markdown(f"<p style='text-align: {alinhamento};'>{texto}</p>", unsafe_allow_html=True)
