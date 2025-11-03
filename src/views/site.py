import streamlit as st
from src.controlers.encriptado import *

p = st.number_input("Digite um primo para p", step=1, value=11)
q = st.number_input("Digite um primo para q", step=1, value=13)
e = st.number_input("Digite o expoente e (coprimo de φ(n))", step=1, value=73)

chaves = validar_numeros(p, q, e)
if isinstance(chaves, str):
    st.error(chaves)
else:
    st.success(f"Chaves privadas: {chaves[0]} e públicas: {chaves[1]}")

fazer = st.selectbox(
    "O que você quer fazer",
    ("Criptografar", "Descriptografar"),
    index=None,
    placeholder="Selecione uma opção",
)

if fazer == "Descriptografar":
    arquivo_download = st.file_uploader("Coloque o código.", type="txt")
    if arquivo_download is not None:
        try:
            texto_down = arquivo_download.getvalue().decode("utf-8")
            codigo_down = [int(n) for n in texto_down.split()]
            texto = descriptografar(codigo_down, chaves[0])
            st.write(texto)
            st.success("Arquivo lido com sucesso!")
        except Exception as e:
            st.error("Ocorreu um erro no arquivo ou a chave é diferente da chave que criptografou")
elif fazer == "Criptografar":
    texto_cript = st.text_input("Texto para ser criptografado")
    p_n = st.number_input("Digite o n da chave pública", step=1, value=143)
    p_e = st.number_input("Digite o e da chave pública", step=1, value=73)
    codigo_crip = criptografar(texto_cript, (p_n, p_e))
    st.write(codigo_crip)
    codigo_string = " ".join(str(n) for n in codigo_crip)
    arquivo_codigo = codigo_string.encode("utf-8")

    st.download_button(
    label="Download Código",
    data=arquivo_codigo,
    file_name="codigo.txt",
    )
    st.success("Texto encriptado com sucesso")