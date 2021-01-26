from flask_restful import Resource
from models.respostas import Resposta
from flask import Flask, jsonify, request

listaRespostas = []

class CadastrarRespostas(Resource):
    @staticmethod
    def post():
        resposta = request.json['resposta']
        provasRespostas = Resposta(resposta['idProva'],
                    resposta['idAluno'],
                    resposta['q1'],
                    resposta['q2'],
                    resposta['q3'],
                    resposta['q4'],
                    resposta['q5'],
                    resposta['q6'],
                    resposta['q7'],
                    resposta['q8'],
                    resposta['q9'],
                    resposta['q10'])
        respostas = {'idProva': provasRespostas.idProva,
                  'idAluno': provasRespostas.idAluno,
                  'q1': provasRespostas.q1,
                  'q2': provasRespostas.q2,
                  'q3': provasRespostas.q3,
                  'q4': provasRespostas.q4,
                  'q5': provasRespostas.q5,
                  'q6': provasRespostas.q6,
                  'q7': provasRespostas.q7,
                  'q8': provasRespostas.q8,
                  'q9': provasRespostas.q9,
                  'q10': provasRespostas.q10}
        listaRespostas.append(provasRespostas)
        return f'Resposta da prova {respostas["idProva"]} cadastrada com sucesso para o aluno {respostas["idAluno"]}.'

    def get(self):
        for i in listaRespostas:
            print("Prova: ",i.idProva)
            print("Aluno: ", i.idAluno)
            print(i.q1)
            print(i.q2)
            print(i.q3)
            print(i.q4)
            print(i.q5)
            print(i.q6)
            print(i.q7)
            print(i.q8)
            print(i.q9)
            print(i.q10)
        return 'lista de respostas'