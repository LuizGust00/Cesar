import sqlite3
import json
import numpy as np

class Usuario:
    def __init__(self, id=None, nome=None, senha=None, chave_n=None, chave_e=None,
                 chave_d=None, logado=None, data_criacao=None, usuario_teste=None, conversas=None):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.chave_n = chave_n
        self.chave_e = chave_e
        self.chave_d = chave_d
        self.logado = logado
        self.data_criacao = data_criacao
        self.usuario_teste = usuario_teste
        self.conversas = conversas

    def __repr__(self):
        return f"<Usuario id={self.id}, nome={self.nome}, chave_n={self.chave_n}, chave_e={self.chave_e}>"

    def adicionar(self, cursor: sqlite3.Cursor):
        if self.id == None:
            cursor.execute('INSERT INTO usuarios (nome, senha, chave_n, chave_e, chave_d) VALUES (?, ?, ?, ?, ?)',
                (self.nome, self.senha, self.chave_n, self.chave_e, self.chave_d))
            self.id = cursor.lastrowid
            print(f"Usuario: <{self.nome}> de id: <{self.id}> foi adicionado com sucesso")
        if self.usuario_teste is not None:
            Usuario.modificar(self.id, cursor, usuario_teste=self.usuario_teste)

    @classmethod
    def modificar(cls, id: int, cursor: sqlite3.Cursor, nome=None, senha=None, chave_n=None,
                  chave_e=None, chave_d=None, logado=None, usuario_teste=None, conversas=None):
        if nome is not None:
            cursor.execute('UPDATE usuarios SET nome = ? WHERE id = ?', (nome, id))
        if senha is not None:
            cursor.execute('UPDATE usuarios SET senha = ? WHERE id = ?', (senha, id))
        if chave_n is not None:
            cursor.execute('UPDATE usuarios SET chave_n = ? WHERE id = ?', (chave_n, id))
        if chave_e is not None:
            cursor.execute('UPDATE usuarios SET chave_e = ? WHERE id = ?', (chave_e, id))
        if chave_d is not None:
            cursor.execute('UPDATE usuarios SET chave_d = ? WHERE id = ?', (chave_d, id))
        if logado is not None:
            cursor.execute('UPDATE usuarios SET logado = ? WHERE id = ?', (logado, id))
        if usuario_teste is not None:
            cursor.execute('UPDATE usuarios SET usuario_teste = ? WHERE id = ?', (usuario_teste, id))
        if conversas is not None:
            cursor.execute('UPDATE usuarios SET conversas = ? WHERE id = ?', (conversas, id))

    @classmethod
    def carregar_usuario(cls, id: int, cursor: sqlite3.Cursor, publico=True):
        if publico:
            dados_brutos = cursor.execute('SELECT id, nome, chave_n, chave_e, logado, data_criacao FROM usuarios WHERE id = ?', (id,))
            dados = dados_brutos.fetchone()
            return Usuario(id=dados[0], nome=dados[1], chave_n=dados[2], chave_e=dados[3], logado=dados[4], data_criacao=dados[5])
        else:
            dados_brutos = cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
            dados = dados_brutos.fetchone()
            return Usuario(id=dados[0], nome=dados[1], senha=dados[2], chave_n=dados[3], chave_e=dados[4],
                           chave_d=dados[5], logado=dados[6], data_criacao=dados[7], usuario_teste=dados[8], conversas=json.loads(dados[9]))
    
    @classmethod
    def achar_id_nome(cls, cursor: sqlite3.Cursor, nome=None, id=None):
        if nome is not None:
            cursor.execute('SELECT id FROM usuarios WHERE nome = ?', (nome,))
            return cursor.fetchone()[0]
        else:
            cursor.execute('SELECT nome FROM usuarios WHERE id = ?', (id,))
            return cursor.fetchone()[0]
    
    @classmethod
    def verificar_senha(cls, cursor: sqlite3.Cursor, senha: str, nome=None, id=None):
        if nome is not None:
            cursor.execute('SELECT senha FROM usuarios WHERE nome = ?', (nome,))
            return (cursor.fetchone()[0] == senha)
        else:
            cursor.execute('SELECT senha FROM usuarios WHERE id = ?', (id,))
            return (cursor.fetchone()[0] == senha)

    @classmethod  
    def usuario_existe(cls, cursor: sqlite3.Cursor, nome: str):
        cursor.execute('SELECT nome FROM usuarios')
        lista_de_usuarios = [item[0] for item in cursor.fetchall()]
        return nome in lista_de_usuarios
    
    @classmethod
    def pegar_dado(cls, id: int, cursor: sqlite3.Cursor, conversas=False):
        if conversas:
            cursor.execute('SELECT conversas FROM usuarios WHERE id = ?', (id,))
            return json.loads(cursor.fetchone()[0])
    
    @classmethod
    def adicionar_conversa(cls, id: int, cursor: sqlite3.Cursor, conversa: int):
        conversa_antiga = []
        cursor.execute('SELECT conversas FROM usuarios WHERE id = ?', (id,))
        dados_bruto = cursor.fetchone()[0]
        conversa_antiga = json.loads(dados_bruto)
        if not conversa in conversa_antiga:
            conversa_antiga.append(conversa)
            cursor.execute('UPDATE usuarios SET conversas = ? WHERE id = ?', (str(conversa_antiga), id))
            
    @classmethod
    def lista_id(cls, cursor: sqlite3.Cursor, excluir=[]):
        cursor.execute('SELECT id FROM usuarios')
        lista_de_id = [item[0] for item in cursor.fetchall()]
        for id_fora in excluir:
            lista_de_id.remove(id_fora)
        return lista_de_id
    

class Chats:
    def __init__(self, id=None, integrantes=None, mensagens=None, data_criacao=None, data_modificacao=None):
        self.id = id
        self.integrantes = integrantes
        self.mensagens = mensagens
        self.data_criacao = data_criacao
        self.mensdata_modificacaoagem_eu = data_modificacao

    @classmethod
    def adicinar_integrantes(cls, id: int, cursor: sqlite3.Cursor, integrantes=[]):
        integrantes_antiga = []
        cursor.execute('SELECT integrantes FROM chats WHERE id = ?', (id,))
        dados_bruto = cursor.fetchone()[0]
        integrantes_antiga = json.loads(dados_bruto)
        if not conversa in integrantes_antiga:
            integrantes_antiga.append(conversa)
            cursor.execute('UPDATE usuarios SET conversas = ? WHERE id = ?', (str(conversa_antiga), id))

