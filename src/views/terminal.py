from ..controlers.encriptado import *
import os

pasta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pasta_textos = os.path.join(pasta_raiz, "textos")
saida_pasta = os.path.join(pasta_textos, "saida")

#Geral
sistema = input("Escolher as chaves manualmente (M) ou automaticamente (A)? ")
if sistema.upper() == 'M':
    p = int(input("Digite um número primo p: "))
    q = int(input("Digite um número primo q: "))
    e = int(input("Digite o expoente e (coprimo de φ(n)): "))
else:
    p = 13
    q = 11
    e = 73

print("-------------------------------------------------------")
print(f"p: {p}, q: {q}, e: {e}")
print("-------------------------------------------------------")
chaves = validar_numeros(p, q, e)
if isinstance(chaves, str):
    print(chaves)
    quit()
print(f"chaves privadas: {chaves[0]} e públicas: {chaves[1]}")
print("-------------------------------------------------------")

def terminal_criptografar():
    texto = input("Digite a mensagem a ser criptografada: ")
    print("-------------------------------------------------------")
    p_n = input("Digite o N da chave publica:")
    p_e = input("Digite o E da chave publica:")
    codigo = criptografar(texto, (int (p_n), int(p_e)))
    nome_arquivo = input("Digite o nome do arquivo de texto (não coloque .txt): ") + ".txt"
    caminho_arquivo = os.path.join(saida_pasta, nome_arquivo)
    gerar_txt(caminho_arquivo, codigo)
    print("-------------------------------------------------------")  

def terminal_descriptografar():
    nome_arquivo = input("Nome do arquivo (não coloque .txt): ") + ".txt"
    print("-------------------------------------------------------")  
    caminho_arquivo = os.path.join(pasta_textos, "entrada_codigo", nome_arquivo)
    codigo = ler_codigo(caminho_arquivo)
    texto = descriptografar(codigo, chaves[0])
    print(texto)
    print("-------------------------------------------------------")  

def terminal_crip_arquivo():
    nome_arquivo = input("Nome do arquivo (não coloque .txt): ") + ".txt"
    print("-------------------------------------------------------")  
    caminho_arquivo = os.path.join(pasta_textos, "entrada_texto", nome_arquivo)
    mesagem = ler_texto(caminho_arquivo)
    codigo = criptografar(mesagem, chaves[1])
    nome_arquivo = input("Digite o nome do arquivo gerado (não coloque .txt): ") + ".txt"
    print("-------------------------------------------------------")  
    caminho_arquivo = os.path.join(saida_pasta, nome_arquivo)
    gerar_txt(caminho_arquivo, codigo)

while True:
    fazer = input("Você vai criptografar (C), descriptografar (D) ou criptografar arquivo (A)? ")
    print("-------------------------------------------------------") 
    if fazer.upper() == 'C':
        terminal_criptografar()
    elif fazer.upper() == 'D':
        terminal_descriptografar()
    elif fazer.upper() == 'A':
        terminal_crip_arquivo()
    else:
        break