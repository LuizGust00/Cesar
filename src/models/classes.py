class Usuario:
    def __init__(self, nome: str,senha: str, chaves: tuple):
        self.nome = nome
        self.senha = senha
        self.chaves= chaves

class Mensagem_PV:
    def __init__(self, nome: str,data: str, hora: str, mensagem_eu: int, mensagem_voce: int):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.mensagem_eu = mensagem_eu
        self.mensagem_destinatario = mensagem_voce

