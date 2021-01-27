
class Aluno():
    respostas = []
    aprovado = False
    def __init__(self, id, nome, cpf, media=0):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.media = media

