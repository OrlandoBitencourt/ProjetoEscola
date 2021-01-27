

#Q = Respostas das perguntas Ex. q1 (resposta da questão 1)

class Resposta():
    def __init__(self, idProva, idAluno, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, nota=0):
        self.idProva = idProva
        self.idAluno = idAluno
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.nota = nota
